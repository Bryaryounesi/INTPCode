import cv2
import matplotlib.pyplot as plt
import torch
import torchvision
from torchvision import transforms, models
from PIL import Image
from pathlib import Path

p = print

# --------------model info------------------
weights = models.ResNet18_Weights.IMAGENET1K_V1
labels = weights.meta["categories"]
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = models.resnet18(weights=weights)
model.to(device)

transform = transforms.Compose(
    [
        transforms.Resize(256),
        transforms.CenterCrop(224),
        transforms.ToTensor(),
        transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
    ]
)

# -----------------------preprocess----------------------
def preprocessing(pil_img):
    tensor = transform(pil_img)
    tensor = tensor.to(device)
    input_batch = tensor.unsqueeze(0)
    return input_batch
# -------------------------model_predict------------------
def model_predict(input_batch, model, k=5):
    model.eval()
    with torch.no_grad():
        outputs = model(input_batch)
        probabilities = torch.softmax(outputs, dim=1)
        top_p, top_i = probabilities.topk(k, dim=1)
        return top_p[0], top_i[0]


# -------------------virsualize-------------------------
def show_image(img, top_p, top_i):
    plt.imshow(img)
    plt.title(f" best class: {labels[top_i[0].item()]}(prob:{top_p[0].item():.2%})")
    plt.axis("off")
    plt.pause(0.5)
# -------------------I/O-------------------------
def read_img(path):
    img = cv2.imread(path)
    if img is None:
        return None
    rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    pil_img = Image.fromarray(rgb_img)
    return pil_img


def save_image(img, top_p, top_i, name, output):
    output.mkdir(parents=True, exist_ok=True)
    fig, ax = plt.subplots(constrained_layout=True)
    ax.imshow(img)
    ax.axis("off")
    ax.set_title(f" best class: {labels[top_i[0].item()]}(prob:{top_p[0].item():.2%})")
    fig.savefig(output / f"{name}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

# -----------------------------main--------------------------
def resnet18_predict(folder, k=3, show_images=True, save_images=True, output = None):
    folder = Path(folder)
    paths = [str(i) for i in folder.glob("*.jpg")]
    for i in paths:
        name = Path(i).stem
        img = read_img(i)
        if img is None:
            p(f"{name} was skipped")
            continue
        input_batch = preprocessing(img)
        top_p, top_i = model_predict(input_batch, model, k)
        # -----------------------report-----------
        for j in range(len(top_p)):
            p(f"{j+1}_{labels[top_i[j].item()]:<40}{top_p[j].item():.2%}")
        p(f"image name: {name}")
        p("------------------------------")
        # -------------------------show_images--------------
        if show_images:
            show_image(img, top_p, top_i)
        # ---------------------------save_images--------------
        if save_images:
            save_image(img, top_p, top_i, name, output)


if __name__ == "__main__":
    folder = Path(
        r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Deep-Learning-Phase\dl-mini-projects\Pretrained_Inference\data"
    )
    output = Path(
        r"E:\python\INTPCode\5_Month_Computer_Vision_Roadmap\Deep-Learning-Phase\dl-mini-projects\Pretrained_Inference\output"
    )
    resnet18_predict(
        folder, k=3, show_images=False, save_images=False, output = output
    )
