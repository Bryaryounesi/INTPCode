class HintsCheatSheet:
    """
    🏷️ [Hints]

    📌 چیت‌شیت تعاملی الگوهای کاربردی پایتون و CV.

    📌 این کلاس فقط شامل الگوهایی است که فایل‌های `.pyi` نمی‌توانند
    هاور کنند: الگوهای ترکیبی، قراردادها، مفاهیم، و اپراتورها به
    شکل اسم‌دار. توابع داخلی و متدها (که `.pyi` هاور می‌کند) در اینجا
    تکرار نشده‌اند.

    📌 مثال استفاده:
        cvt.h.if_conf     → الگوی شرط روی confidence
        cvt.h.for_enum    → پیمایش با ایندکس
        cvt.h.f_pad       → شماره‌گذاری با صفر در f-string
    """

    # ------------------------------------------
    # شرط‌ها
    # ------------------------------------------
    @property
    def if_conf(self):
        """
        📌 [CV] شرط روی confidence.

        📌 پذیرش پیش‌بینی مطمئن:
        if confidence > 0.7:
            accept()

        📌 رد پیش‌بینی نامطمئن:
        if confidence < 0.5:
            reject()

        📌 سه سطحی:
        if conf >= 0.9:
            label = "high"
        elif conf >= 0.7:
            label = "medium"
        else:
            label = "low"
        """
        return "if conf > 0.7"

    @property
    def if_none(self):
        """
        📌 [CV] بررسی None.

        📌 رد تصویر خراب:
        img = cv2.imread(path)
        if img is None:
            print(f"failed: {path}")
            continue

        📌 مقدار پیش‌فرض برای None:
        value = data.get("confidence")
        if value is None:
            value = 0.0

        📌 قاعده: همیشه `is None` بنویس، نه `== None`.
        """
        return "if img is None"

    @property
    def if_in(self):
        """
        📌 [CV] بررسی عضویت.

        📌 بررسی وجود لیبل در لیست یونیک:
        if label in unique_labels:
            pass

        📌 بررسی پسوند فایل:
        if path.suffix in {".jpg", ".png"}:
            pass

        📌 بررسی وجود کلید در دیکشنری:
        if "confidence" in item:
            pass
        """
        return "if x in data"

    @property
    def if_empty(self):
        """
        📌 [CV] بررسی خالی بودن.

        📌 لیست خالی:
        if not image_paths:
            print("no images found")
            return

        📌 دیکشنری خالی:
        if not dataset:
            return

        📌 رشته خالی:
        if not label:
            label = "unknown"

        📌 قاعده: هر مقدار falsy (0, "", [], {}, None, False)
        در if معادل False است. پس `if not x` بنویس، نه
        `if len(x) == 0`.
        """
        return "if not data"

    @property
    def if_and(self):
        """
        📌 [CV] ترکیب شرط‌ها با and.

        📌 بررسی چند شرط:
        if age >= 18 and has_permit:
            drive()

        📌 [CV] فیلتر دیتاست:
        if item["confidence"] > 0.7 and item["label"] == "cat":
            pass

        📌 نکته: پایتون هر دو طرف را ارزیابی می‌کند (short-circuit).
        """
        return "if a and b"

    @property
    def if_or(self):
        """
        📌 [CV] ترکیب شرط‌ها با or.

        📌 [CV] رد تصویر خراب:
        if img is None or img.size == 0:
            continue

        📌 مقدار پیش‌فرض:
        label = data.get("label") or "unknown"

        📌 نکته: هر دو طرف را با هم یا جداگانه می‌شود استفاده کرد.
        """
        return "if a or b"

    @property
    def if_ternary(self):
        """
        📌 [CV] شرط یک‌خطی (ternary).

        📌 انتخاب بین دو مقدار:
        status = "adult" if age >= 18 else "minor"

        📌 [CV] وضعیت پردازش:
        status = "OK" if confidence > 0.7 else "low"

        📌 [CV] مقدار پیش‌فرض:
        label = data["label"] if "label" in data else "unknown"

        📌 معادل:
        if age >= 18:
            status = "adult"
        else:
            status = "minor"
        """
        return "x if cond else y"

    # ------------------------------------------
    # حلقه‌ها
    # ------------------------------------------
    @property
    def for_enum(self):
        """
        📌 [CV] پیمایش دیتاست با ایندکس.

        📌 پایه:
        for idx, path in enumerate(image_paths):
            print(f"processing {idx}: {path}")

        📌 با شمارنده از 1:
        for i, item in enumerate(items, start=1):
            print(f"{i}. {item}")

        📌 [CV] پیمایش دو لیست با ایندکس:
        for idx, (img, label) in enumerate(zip(images, labels)):
            print(f"sample {idx}: {img} → {label}")
        """
        return "for idx, x in enumerate(data)"

    @property
    def for_zip(self):
        """
        📌 [CV] جفت کردن دو لیست.

        📌 تصویر و لیبل:
        for img_path, label in zip(image_paths, labels):
            print(f"{img_path} → {label}")

        📌 [CV] prediction و ground truth:
        for pred, true in zip(predictions, ground_truths):
            compare(pred, true)

        📌 نکته: zip از کوتاه‌ترین لیست پیروی می‌کند.
        """
        return "for a, b in zip(x, y)"

    @property
    def for_batch(self):
        """
        📌 [CV] پردازش دسته‌ای (batch).

        📌 پایه:
        batch_size = 32
        for i in range(0, len(paths), batch_size):
            batch = paths[i:i+batch_size]
            process(batch)

        📌 ساخت batch با generator:
        def batches(data, size):
            for i in range(0, len(data), size):
                yield data[i:i+size]
        """
        return "for i in range(0, n, step)"

    @property
    def for_dict(self):
        """
        📌 [CV] پیمایش دیکشنری.

        📌 کلید و مقدار:
        for key, value in item.items():
            print(f"{key}: {value}")

        📌 فقط کلید:
        for key in item:
            print(key)

        📌 فقط مقدار:
        for value in item.values():
            print(value)

        📌 [CV] پیمایش label_map:
        for label, idx in label_map.items():
            print(f"{label} → {idx}")
        """
        return "for k, v in data.items()"

    @property
    def for_break_continue(self):
        """
        📌 [CV] کنترل حلقه.

        📌 break — خروج کامل:
        for img in paths:
            if img == "target.jpg":
                break

        📌 continue — رد کردن این دور:
        for path in paths:
            if path.endswith(".png"):
                continue
            process(path)

        📌 [CV] الگوی رایج: continue برای فایل خراب.
        """
        return "break / continue"

    @property
    def for_else(self):
        """
        📌 [CV] else در حلقه.

        📌 else اجرا می‌شود فقط اگر break نزنی:
        for img in paths:
            if is_valid(img):
                break
        else:
            print("no valid image found")

        📌 کاربرد: پیدا کردن مورد خاص، اجرای fallback اگر نبود.
        """
        return "for ... else ..."

    # ------------------------------------------
    # فایل و context manager
    # ------------------------------------------
    @property
    def with_open(self):
        """
        📌 [CV] باز کردن فایل با context manager.

        📌 خواندن تصویر باینری:
        with open("image.jpg", "rb") as f:
            data = f.read()

        📌 [CV] خواندن لیبل‌ها:
        with open("labels.txt", "r", encoding="utf-8") as f:
            labels = [line.strip() for line in f]

        📌 [CV] نوشتن نتایج:
        with open("results.txt", "w", encoding="utf-8") as f:
            f.write(f"accuracy: {acc:.4f}\\n")

        📌 قاعده: with تضمین می‌کند فایل حتی در صورت خطا
        بسته شود. بدون with، فایل باز می‌ماند.
        """
        return "with open(...) as f"

    @property
    def with_pandas(self):
        """
        📌 [CV] خواندن/نوشتن CSV.

        📌 خواندن:
        import pandas as pd
        df = pd.read_csv("annotations.csv")

        📌 نوشتن:
        df.to_csv("results.csv", index=False)

        📌 [CV] خواندن CSV بدون pandas:
        import csv
        with open("labels.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                print(row["image"], row["label"])
        """
        return "with open(...) / csv"

    @property
    def try_file(self):
        """
        📌 [CV] خواندن ایمن فایل.

        📌 ساده:
        try:
            with open(path, "rb") as f:
                data = f.read()
        except FileNotFoundError:
            print(f"not found: {path}")
            return None

        📌 [CV] الگوی کامل با چند خطا:
        try:
            with open(path, "rb") as f:
                data = f.read()
        except FileNotFoundError:
            print(f"not found: {path}")
            return None
        except PermissionError:
            print(f"no permission: {path}")
            return None
        except Exception as e:
            print(f"error: {e}")
            return None
        """
        return "try/except FileNotFoundError"

    @property
    def try_safe_load(self):
        """
        📌 [CV] خواندن ایمن تصویر در حلقه.

        📌 الگوی رایج:
        for path in paths:
            try:
                img = cv2.imread(path)
                if img is None:
                    raise ValueError(f"failed to load {path}")
                process(img)
            except Exception as e:
                print(f"skipping {path}: {e}")
                continue

        📌 [CV] نکته: continue باعث می‌شود بقیه دیتاست
        پردازش شود، نه اینکه کل حلقه متوقف شود.
        """
        return "try/except در حلقه"

    # ------------------------------------------
    # f-string
    # ------------------------------------------
    @property
    def f_2f(self):
        """
        📌 فرمت اعشار دو رقمی.

        📌 [CV] نمایش accuracy:
        print(f"accuracy: {acc:.2f}")     # 0.96

        📌 [CV] نمایش loss:
        print(f"loss: {loss:.4f}")         # 0.0234

        📌 فرمت کلی: f"{value:.Nf}" که N تعداد اعشار است.
        """
        return 'f"{value:.2f}"'

    @property
    def f_pct(self):
        """
        📌 فرمت درصد.

        📌 [CV] نمایش precision:
        print(f"precision: {p:.1%}")     # 95.7%

        📌 دو رقم اعشار درصد:
        print(f"precision: {p:.2%}")     # 95.68%
        """
        return 'f"{value:.1%}"'

    @property
    def f_pad(self):
        """
        📌 شماره‌گذاری با صفر.

        📌 [CV] نام‌گذاری تصویر:
        for idx in range(5):
            print(f"image_{idx:04d}.jpg")
        # image_0000.jpg, image_0001.jpg, ..., image_0004.jpg

        📌 فرمت کلی: f"{value:0Nd}" که N تعداد کل ارقام است.
        """
        return 'f"image_{idx:04d}.jpg"'

    @property
    def f_align(self):
        """
        📌 تراز در f-string.

        📌 راست‌چین:
        f"|{name:>10}|"     # |     yolo|

        📌 چپ‌چین:
        f"|{name:<10}|"     # |yolo     |

        📌 وسط‌چین:
        f"|{name:^10}|"     # |  yolo   |

        📌 [CV] جدول متریک‌ها:
        for name, acc in results:
            print(f"{name:<15} acc: {acc:>6.2%}")
        """
        return 'f"{value:>10}" / :<10 / :^10'

    @property
    def f_inline_expr(self):
        """
        📌 عبارت داخل f-string.

        📌 فراخوانی متد:
        f"{name.upper()}"
        f"{path.stem}"

        📌 [CV] attribute:
        f"{image.shape}"       # (1080, 1920, 3)
        f"{img.shape[0]}"      # 1080

        📌 [CV] شرط یک‌خطی:
        f"{'OK' if conf > 0.7 else 'low'}"

        📌 دیکشنری:
        f"{data['label']}"
        """
        return 'f"{expr}"'

    @property
    def f_braces(self):
        """
        📌 نمایش خود کاراکتر { } در f-string.

        📌 فرار:
        f"{{literal braces}}"    # {literal braces}

        📌 نکته: داخل {} می‌شود هر عبارت معتبر پایتون نوشت.
        برای نمایش خود آکولاد، دو تا بنویس: {{ و }}.
        """
        return 'f"{{...}}"'

    @property
    def f_repr(self):
        """
        📌 نمایش repr و str در f-string.

        📌 پیش‌فرض (str):
        f"{name}"      # yolo

        📌 با !r (repr):
        f"{name!r}"    # 'yolo'

        📌 تفاوت: repr برای دیباگ (با کوتیشن)، str برای
        نمایش کاربر.
        """
        return 'f"{value!r}"'

    # ------------------------------------------
    # کامپرهنشن
    # ------------------------------------------
    @property
    def lc_transform(self):
        """
        📌 [CV] تبدیل با list comprehension.

        📌 [CV] نرمال‌سازی پیکسل:
        normalized = [p / 255 for p in pixels]

        📌 [CV] افزایش روشنایی:
        brightened = [p + 30 for p in pixels]

        📌 [CV] تبدیل درجه:
        fahrenheit = [(c * 9/5) + 32 for c in celsius]

        📌 معادل با حلقه:
        result = []
        for x in data:
            result.append(func(x))
        """
        return "[func(x) for x in data]"

    @property
    def lc_filter(self):
        """
        📌 [CV] فیلتر با list comprehension.

        📌 [CV] فیلتر پسوند فایل:
        jpgs = [f for f in files if f.endswith(".jpg")]

        📌 [CV] فیلتر confidence:
        good = [item for item in dataset if item["confidence"] > 0.7]

        📌 [CV] فیلتر محدوده:
        bright = [p for p in pixels if 100 < p < 240]

        📌 معادل با حلقه:
        result = []
        for x in data:
            if condition(x):
                result.append(x)
        """
        return "[x for x in data if condition]"

    @property
    def lc_filter_transform(self):
        """
        📌 [CV] ترکیب فیلتر و تبدیل.

        📌 [CV] تبدیل فقط مقادیر بالا:
        hot_f = [(t * 9/5) + 32 for t in temperatures if t > 25]

        📌 [CV] فقط تصاویر موجود:
        valid = [load(p) for p in paths if Path(p).exists()]
        """
        return "[func(x) for x in data if condition]"

    @property
    def lc_if_else(self):
        """
        📌 [CV] شرطی با if-else (تعداد خروجی حفظ می‌شود).

        📌 [CV] ساخت ماسک باینری:
        mask = [1 if p > 100 else 0 for p in pixels]

        📌 [CV] نرمال‌سازی شرطی:
        normalized = [p / 255 if p > 0 else 0 for p in pixels]

        📌 نکته: اگر else نداشته باشد، خطا می‌دهد.
        خروجی به اندازه ورودی است (هیچ حذفی نیست).
        """
        return "[A if cond else B for x in data]"

    @property
    def lc_nested(self):
        """
        📌 [CV] list comprehension تودرتو (تصویر 2D).

        📌 [CV] فلت کردن تصویر (2D → 1D):
        flat = [pixel for row in image_2d for pixel in row]

        📌 [CV] افزایش روشنایی با حفظ ساختار:
        brightened = [[p + 10 for p in row] for row in image_2d]

        📌 [CV] ساخت ماسک باینری:
        mask = [[1 if p > 100 else 0 for p in row] for row in image_2d]

        📌 نکته: حلقه اول بیرونی، حلقه دوم داخلی.
        """
        return "[[f(p) for p in row] for row in image]"

    @property
    def dc_transform(self):
        """
        📌 [CV] dict comprehension.

        📌 [CV] label encoding:
        label_map = {label: i for i, label in enumerate(labels)}

        📌 [CV] تبدیل ساختار:
        scaled = {k: [v * 2 for v in box] for k, box in boxes.items()}

        📌 معادل با حلقه:
        result = {}
        for k, v in data.items():
            result[k] = func(v)
        """
        return "{k: func(v) for k, v in data.items()}"

    @property
    def dc_filter(self):
        """
        📌 [CV] فیلتر دیکشنری.

        📌 [CV] فیلتر annotation بر اساس confidence:
        filtered = {k: v for k, v in annotations.items() if v > 0.5}

        📌 [CV] فقط تصاویر معتبر:
        valid = {k: v for k, v in data.items() if v is not None}
        """
        return "{k: v for k, v in data.items() if cond}"

    @property
    def gen_expr(self):
        """
        📌 [CV] generator expression.

        📌 [CV] صرفه‌جویی حافظه:
        gen = (p * 2 for p in pixels)

        📌 تفاوت با list:
        [x for x in data]  →  حافظه می‌گیرد، همه محاسبه می‌شود
        (x for x in data)  →  حافظه کم، یکی‌یکی محاسبه می‌شود

        📌 [CV] برای دیتاست بزرگ تصاویر، generator بهتر است.
        """
        return "(x for x in data)"

    @property
    def sort_key(self):
        """
        📌 [CV] مرتب‌سازی با کلید سفارشی.

        📌 [CV] مرتب‌سازی بر اساس confidence:
        samples.sort(key=lambda x: x["confidence"], reverse=True)

        📌 [CV] مرتب‌سازی contours بر اساس مساحت:
        sorted_contours = sorted(contours, key=cv2.contourArea, reverse=True)

        📌 [CV] مرتب‌سازی مسیرها بر اساس نام:
        sorted(files, key=lambda p: p.name)

        📌 تفاوت sort و sorted:
        list.sort()    →  درجا، None برمی‌گرداند
        sorted(list)   →  لیست جدید، اصلی دست‌نخورده
        """
        return "sort(key=lambda x: ...)"

    # ------------------------------------------
    # اپراتورها به شکل اسم‌دار
    # ------------------------------------------
    @property
    def op_gt(self):
        """
        📌 بزرگ‌تر از.

        📌 [CV] فیلتر confidence:
        if confidence > 0.7:
            accept()

        📌 [CV] فیلتر روشنایی:
        bright = [p for p in pixels if p > 100]
        """
        return ">"

    @property
    def op_lt(self):
        """
        📌 کوچک‌تر از.

        📌 [CV] توقف زودهنگام:
        if loss < 0.01:
            stop()

        📌 [CV] فیلتر روشنایی:
        dark = [p for p in pixels if p < 50]
        """
        return "<"

    @property
    def op_ge(self):
        """
        📌 بزرگ‌تر یا مساوی.

        📌 [CV] آستانه:
        if age >= 18:
            pass

        📌 [CV] حداقل اطمینان:
        if conf >= 0.9:
            label = "high"
        """
        return ">="

    @property
    def op_le(self):
        """
        📌 کوچک‌تر یا مساوی.

        📌 [CV] هشدار باتری:
        if battery <= 20:
            warn()
        """
        return "<="

    @property
    def op_eq(self):
        """
        📌 برابر.

        📌 [CV] بررسی لیبل:
        if label == "cat":
            pass

        📌 [CV] بررسی پسوند:
        if path.suffix == ".jpg":
            pass
        """
        return "=="

    @property
    def op_ne(self):
        """
        📌 نابرابر.

        📌 [CV] رد پس‌زمینه:
        if label != "background":
            pass
        """
        return "!="

    @property
    def op_div(self):
        """
        📌 تقسیم (float).

        📌 [CV] نرمال‌سازی پیکسل:
        normalized = pixel / 255

        📌 نتیجه: float. اگر int می‌خواهی از // استفاده کن.
        """
        return "/"

    @property
    def op_floordiv(self):
        """
        📌 تقسیم صحیح.

        📌 [CV] نصف کردن ابعاد:
        half_h = h // 2
        half_w = w // 2

        📌 [CV] مرکز تصویر:
        cy, cx = h // 2, w // 2
        """
        return "//"

    @property
    def op_mod(self):
        """
        📌 باقی‌مانده.

        📌 [CV] بررسی زوج/فرد:
        if idx % 2 == 0:
            pass

        📌 [CV] چرخش بین N گزینه:
        color = colors[idx % len(colors)]
        """
        return "%"

    @property
    def op_pow(self):
        """
        📌 توان.

        📌 [CV] مساحت دایره:
        area = 3.14159 * r ** 2

        📌 [CV] فاصله اقلیدسی (تک بعد):
        distance = (a - b) ** 2
        """
        return "**"

    @property
    def op_matmul(self):
        """
        📌 ضرب ماتریسی.

        📌 [CV] ضرب ماتریسی NumPy:
        C = A @ B

        📌 معادل:
        C = np.matmul(A, B)
        C = np.dot(A, B)

        📌 نکته: @ فقط در پایتون 3.5+ کار می‌کند.
        """
        return "@"

    @property
    def op_walrus(self):
        """
        📌 عملگر والرس (تخصیص در عبارت).

        📌 استفاده در شرط:
        if (n := len(paths)) > 0:
            print(f"found {n} paths")

        📌 استفاده در while:
        while (line := f.readline()):
            process(line)

        📌 نکته: در پایتون 3.8+ موجود است.
        """
        return ":="

    @property
    def op_arrow(self):
        """
        📌 نوع بازگشتی تابع.

        📌 [CV] تابع با تایپ مشخص:
        def load(path) -> np.ndarray:
            return cv2.imread(path)

        📌 بدون مقدار برگشتی:
        def display(img) -> None:
            cv2.imshow("win", img)
        """
        return "->"

    @property
    def op_augmented(self):
        """
        📌 عملگرهای انتساب ترکیبی.

        📌 [CV] شمارش:
        count += 1

        📌 [CV] کاهش:
        lives -= 1

        📌 [CV] تجمعی:
        total += sum(areas)

        📌 لیست:
        paths += new_paths    # الحاق درجا
        """
        return "+= / -= / *= / /="

    @property
    def op_bitwise(self):
        """
        📌 عملگرهای بیت‌وایز.

        📌 [CV] خواندن کلید OpenCV:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        📌 [CV] ترکیب ماسک‌ها:
        combined = mask1 | mask2
        diff = mask1 ^ mask2
        inverted = ~mask

        📌 [CV] استخراج کانال رنگ:
        red = pixel >> 16
        green = (pixel >> 8) & 0xFF
        blue = pixel & 0xFF
        """
        return "& | ^ ~ << >>"

    # ------------------------------------------
    # قراردادها و مفاهیم
    # ------------------------------------------
    @property
    def naming(self):
        """
        📌 قراردادهای نام‌گذاری پایتون.

        📌 متغیر و تابع: snake_case
        image_path, load_image, model_name

        📌 ثابت‌ها: UPPER_CASE
        MAX_SIZE = 512, IMAGE_DIR = "data/train"

        📌 کلاس‌ها: PascalCase
        ImageDataset, DataLoader, CVTools

        📌 متد خصوصی: _leading_underscore
        def _generate_id(self): ...

        📌 غلط‌های رایج:
        greating → greeting
        tempreture → temperature
        """
        return "snake_case / PascalCase"

    @property
    def main_guard(self):
        """
        📌 ساختار اسکریپت قابل اجرا.

        📌 الگو:
        def main():
            print("hello CV")

        if __name__ == "__main__":
            main()

        📌 چرا: این خط تضمین می‌کند کد فقط وقتی مستقیم اجرا
        شود اجرا شود، نه وقتی به عنوان ماژول import می‌شود.

        📌 [CV] اسکریپت‌های CV معمولاً هم قابل اجرا هستند
        هم قابل import از فایل‌های دیگر.
        """
        return 'if __name__ == "__main__":'

    @property
    def docstring(self):
        """
        📌 مستندسازی تابع.

        📌 فرمت ساده:
        def load_image(path):
            \"\"\"
            خواندن تصویر از مسیر.

            Parameters:
            - path: مسیر فایل تصویر

            Returns:
            - تصویر خوانده‌شده یا None
            \"\"\"
            return cv2.imread(path)

        📌 نکته: docstring اولین چیزی است که Pylance روی
        تابع هاور می‌کند.
        """
        return '"""docstring"""'

    @property
    def type_hint(self):
        """
        📌 type hints.

        📌 امضای تابع:
        def load(path: str) -> np.ndarray:
            return cv2.imread(path)

        📌 متغیر:
        count: int = 0
        paths: list[str] = []

        📌 Optional:
        def find(id: int) -> Optional[dict]:
            ...

        📌 Union:
        value: Union[int, float] = 0

        📌 نکته: Pylance اینا رو برای type checking استفاده می‌کند.
        """
        return "name: type = value"

    @property
    def truthy_falsy(self):
        """
        📌 مقادیر falsy در پایتون.

        📌 لیست کامل:
        0, 0.0, 0j, "", [], {}, (), set(), None, False

        📌 [CV] مثال:
        if not image_paths:      # لیست خالی
            return

        if not label:            # رشته خالی
            label = "unknown"

        📌 قاعده: در شرط، همیشه `if x` بنویس نه `if x == True`،
        و `if not x` بنویس نه `if len(x) == 0`.
        """
        return "falsy: 0, '', [], {}, None, False"

    @property
    def slice_syntax(self):
        """
        📌 برش در پایتون.

        📌 [CV] برش 1D:
        arr[2:6]         # عناصر 2 تا 5
        arr[:4]          # 4 عنصر اول
        arr[7:]          # از 7 تا آخر
        arr[::2]         # یک در میان
        arr[::-1]        # معکوس

        📌 [CV] برش 2D (تصویر):
        roi = img[y1:y2, x1:x2]

        📌 [CV] برش مرکزی 50%:
        h, w = img.shape[:2]
        center = img[h//4:3*h//4, w//4:3*w//4]

        📌 تفاوت با range:
        range(start, stop, step)  →  تابع، آرگومان‌ها با کاما
        list[start:stop:step]     →  عملگر، با دونقطه
        """
        return "list[start:stop:step]"

    @property
    def unpacking(self):
        """
        📌 unpacking در پایتون.

        📌 تاپل:
        x, y = (10, 20)
        a, b, c = 1, 2, 3

        📌 [CV] از تابع:
        total, avg, mx, mn = calculate_stats(scores)

        📌 با *:
        first, *rest = [1, 2, 3, 4, 5]
        # first=1, rest=[2, 3, 4, 5]

        📌 [CV] در حلقه:
        for x, y in points:
            plot(x, y)

        📌 [CV] تودرتو:
        for name, (chem, eco, math) in students:
            ...
        """
        return "a, b = x, y"

    @property
    def zip_star(self):
        """
        📌 استفاده از * در zip.

        📌 ترانهاده ماتریس:
        rows = [[1, 2], [3, 4], [5, 6]]
        cols = list(zip(*rows))
        # [(1, 3, 5), (2, 4, 6)]

        📌 [CV] ترکیب کانال‌ها:
        r, g, b = img[..., 0], img[..., 1], img[..., 2]
        combined = list(zip(r.ravel(), g.ravel(), b.ravel()))
        """
        return "zip(*data)"

    @property
    def f_string_basics(self):
        """
        📌 f-string — سینتکس پایه.

        📌 متغیر:
        f"name: {name}"

        📌 عبارت:
        f"sum: {a + b}"

        📌 فراخوانی متد:
        f"upper: {name.upper()}"

        📌 [CV] مسیر فایل:
        f"data/{folder}/{name}.jpg"

        📌 نکته: f-string از پایتون 3.6 به بعد موجود است.
        روش قدیمی: "{}".format(value)
        """
        return 'f"...{var}..."'

    @property
    def nested_dict(self):
        """
        📌 دیکشنری تودرتو.

        📌 [CV] ساختار annotation:
        data = {
            "img1.jpg": {
                "label": "cat",
                "bbox": [10, 20, 30, 40],
                "confidence": 0.95
            }
        }

        📌 دسترسی:
        label = data["img1.jpg"]["label"]

        📌 دسترسی امن:
        label = data.get("img1.jpg", {}).get("label", "unknown")

        📌 [CV] پیمایش:
        for img_path, info in data.items():
            print(f"{img_path}: {info['label']}")
        """
        return "data[k1][k2] / .get(k, {})"

    @property
    def enumerate_start(self):
        """
        📌 شمارنده از عدد دلخواه.

        📌 [CV] شماره‌گذاری از 1:
        for i, name in enumerate(files, start=1):
            print(f"{i}. {name}")

        📌 معادل بدون enumerate:
        for i in range(len(files)):
            print(f"{i+1}. {files[i]}")
        """
        return "enumerate(data, start=1)"

    @property
    def list_vs_tuple(self):
        """
        📌 تفاوت لیست و تاپل.

        📌 لیست — تغییرپذیر:
        paths = ["a.jpg", "b.jpg"]
        paths.append("c.jpg")     # مجاز

        📌 تاپل — تغییرناپذیر:
        bbox = (10, 20, 30, 40)
        bbox[0] = 100             # TypeError

        📌 [CV] کجا از تاپل:
        - مختصات، bounding box
        - بازگرداندن چند مقدار از تابع
        - کلید دیکشنری (لیست نمی‌تواند کلید باشد)

        📌 تبدیل:
        tuple([1, 2, 3])          # (1, 2, 3)
        list((1, 2, 3))           # [1, 2, 3]
        """
        return "list (mutable) vs tuple (immutable)"

    @property
    def dict_vs_set(self):
        """
        📌 تفاوت دیکشنری و مجموعه.

        📌 دیکشنری — کلید-مقدار:
        data = {"label": "cat", "conf": 0.95}
        data["label"]             # 'cat'

        📌 مجموعه — فقط کلید یونیک:
        labels = {"cat", "dog", "cat"}   # {'cat', 'dog'}
        "cat" in labels           # True

        📌 [CV] کجا از set:
        unique = set(labels)      # حذف تکراری‌ها
        valid = {"cat", "dog"}    # بررسی عضویت سریع

        📌 نکته: {} دیکشنری است، set() مجموعه.
        """
        return "dict {k: v} vs set {v}"

    @property
    def lambda_basics(self):
        """
        📌 lambda — تابع یک‌خطی بدون نام.

        📌 پایه:
        double = lambda x: x * 2
        double(5)                 # 10

        📌 [CV] sort با کلید:
        samples.sort(key=lambda s: s["confidence"], reverse=True)

        📌 [CV] max با کلید:
        best = max(predictions, key=lambda x: x[1])

        📌 [CV] filter:
        valid = filter(lambda p: p.endswith(".jpg"), files)

        📌 نکته: برای توابع ساده. برای توابع پیچیده از def.
        """
        return "lambda x: expr"

    @property
    def class_basics(self):
        """
        📌 کلاس — ساختار پایه.

        📌 [CV] دیتاست سفارشی:
        class ImageDataset:
            def __init__(self, paths, labels):
                self.paths = paths
                self.labels = labels

            def __len__(self):
                return len(self.paths)

            def __getitem__(self, idx):
                return self.paths[idx], self.labels[idx]

        📌 استفاده:
        dataset = ImageDataset(["a.jpg"], ["cat"])
        len(dataset)              # 1
        dataset[0]                # ('a.jpg', 'cat')
        """
        return "class Name: def __init__(self, ...)"

    @property
    def inheritance_basics(self):
        """
        📌 ارث‌بری.

        📌 [CV] مدل سفارشی:
        class BaseModel:
            def predict(self, x):
                raise NotImplementedError

        class MyModel(BaseModel):
            def __init__(self):
                super().__init__()

            def predict(self, x):
                return x * 2

        📌 نکته: super() برای فراخوانی متد کلاس والد.
        """
        return "class Child(Parent): super().__init__()"

    @property
    def global_keyword(self):
        """
        📌 کلیدواژه global.

        📌 نیاز به global:
        counter = 0

        def increment():
            global counter
            counter += 1

        📌 ⚠️ استفاده از global توصیه نمی‌شود. راه بهتر:
        def increment(counter):
            return counter + 1

        counter = increment(counter)
        """
        return "global var"

    @property
    def f_string_in_path(self):
        """
        📌 [CV] ساخت مسیر فایل با f-string.

        📌 ساخت مسیر:
        f"data/{folder}/{name}.jpg"
        f"outputs/{name}_result.jpg"
        f"image_{idx:04d}.jpg"

        📌 ⚠️ از الحاق با + خودداری کن:
        ❌ "data/" + folder + "/" + name + ".jpg"
        ✅ f"data/{folder}/{name}.jpg"

        📌 برای مسیر کراس‌پلتفرم از pathlib استفاده کن:
        from pathlib import Path
        path = Path("data") / folder / f"{name}.jpg"
        """
        return 'f"data/{folder}/{name}.jpg"'
