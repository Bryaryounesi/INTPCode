
# Object Extraction

A standard object extraction project with proper folder structure and requirements file.

## Pipeline

Image Reading → Grayscale → Threshold → Contour → Object Selection → [Branch: BoundingBox | Mask | Crop] → Save Output

## Outputs

- Mask
- Crop
- Bounding-box

## Project Structure

object-extraction/
├── src/
├── data/
├── outputs/
└── dependencies.txt

## Requirements

Install dependencies:

pip install -r dependencies.txt

## Usage

Run the main script:

python src/main.py

## License

MIT
