{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zCj8cVKT5H8X",
        "outputId": "243c1ddc-c3ca-40ee-ba6f-a6ae1ff1d074"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Failed to capture frame. Exiting...\n",
            "All quadrants saved.\n"
          ]
        }
      ],
      "source": [
        "import cv2\n",
        "import os\n",
        "\n",
        "save_dir = 'Captures'\n",
        "os.makedirs(save_dir, exist_ok=True)\n",
        "\n",
        "cap = cv2.VideoCapture(0)\n",
        "capture_count = 1\n",
        "\n",
        "while True:\n",
        "    ret, frame = cap.read()\n",
        "\n",
        "    if not ret:\n",
        "        print(\"Failed to capture frame. Exiting...\")\n",
        "        break\n",
        "\n",
        "    key = cv2.waitKey(1) & 0xFF\n",
        "\n",
        "    if key == ord('c'):\n",
        "        image_path = os.path.join(save_dir, f\"image{capture_count}.jpg\")\n",
        "        cv2.imwrite(image_path, frame)\n",
        "        print(f\"Captured and saved: {image_path}\")\n",
        "        capture_count += 1\n",
        "\n",
        "    if key == ord('q'):\n",
        "        print(\"Terminating...\")\n",
        "        break\n",
        "\n",
        "cap.release()\n",
        "\n",
        "for i in range(1, capture_count):\n",
        "    image_path = os.path.join(save_dir, f\"image{i}.jpg\")\n",
        "    img = cv2.imread(image_path)\n",
        "\n",
        "    if img is None:\n",
        "        print(f\"Error loading {image_path}. Skipping...\")\n",
        "        continue\n",
        "\n",
        "    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)\n",
        "\n",
        "    h, w = gray_img.shape\n",
        "\n",
        "    quadrant1 = gray_img[0:h//2, 0:w//2]\n",
        "    quadrant2 = gray_img[0:h//2, w//2:w]\n",
        "    quadrant3 = gray_img[h//2:h, 0:w//2]\n",
        "    quadrant4 = gray_img[h//2:h, w//2:w]\n",
        "\n",
        "    cv2.imwrite(os.path.join(save_dir, f\"image{i}_quadrant1.jpg\"), quadrant1)\n",
        "    cv2.imwrite(os.path.join(save_dir, f\"image{i}_quadrant2.jpg\"), quadrant2)\n",
        "    cv2.imwrite(os.path.join(save_dir, f\"image{i}_quadrant3.jpg\"), quadrant3)\n",
        "    cv2.imwrite(os.path.join(save_dir, f\"image{i}_quadrant4.jpg\"), quadrant4)\n",
        "\n",
        "print(\"All quadrants saved.\")\n"
      ]
    }
  ]
}
