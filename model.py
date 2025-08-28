from ultralytics import YOLO
import shutil
import os
from pathlib import Path


def main(input_dir, output_dir):
    # Load Model
    model_path = Path("model") / "THFSS.pt"
    model = YOLO(str(model_path))
    model.to("cpu")
    conf_threshold = 0.7


    # Initialization input and output directory 
    input_directory = Path(input_dir)
    output_directory = Path(output_dir)
    output_directory.mkdir(exist_ok=True)

    for image_file in os.listdir(input_directory):
        if image_file.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = input_directory / image_file

            results = model.predict(image_path, conf=conf_threshold, verbose=False)

            for result in results:
                predictions = []
                for box in result.boxes:
                    pred_data = {
                        'class': int(box.cls.item()),
                        'conf': float(box.conf.item()),
                        'coords': box.xyxy[0].cpu().numpy()
                    }
                    predictions.append(pred_data)

                photo_person = []
                characters_on_photo = []

                for pred in predictions:
                    if pred['conf'] >= conf_threshold:
                        photo_person.append(pred["class"])

                if len(photo_person) == 0:
                    path = output_directory / "Undetected"
                    path.mkdir(exist_ok=True)
                    shutil.copy(input_directory / image_file, path)
                    continue
                else:
                    if (1 in photo_person) or (2 in photo_person):
                        characters_on_photo.append("Senko")

                    if (4 in photo_person) or (5 in photo_person and not 2 in photo_person and not 1 in photo_person):
                        characters_on_photo.append("Shiro")

                    if (7 in photo_person) or (8 in photo_person):
                        characters_on_photo.append("Sora")
                

                if len(characters_on_photo) == 0 and len(photo_person) > 0:
                    path = output_directory / "Undetected"
                    path.mkdir(exist_ok=True)
                    shutil.copy(input_directory / image_file, path)
                    continue


                characters_on_photo = list(set(characters_on_photo))
                characters_on_photo.sort()

                if len(characters_on_photo) == 1:
                    path = output_directory / "The Helpful Fox Senko-san" / characters_on_photo[0]
                    path.mkdir(parents=True, exist_ok=True)
                    shutil.copy(input_directory / image_file, path)

                else:
                    names = "&".join(characters_on_photo)
                    path = output_directory / "The Helpful Fox Senko-san" / names
                    path.mkdir(parents=True, exist_ok=True)
                    shutil.copy(input_directory / image_file, path)


if __name__ == "__main__":
    main()