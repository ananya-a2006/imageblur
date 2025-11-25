# blur_image.py
import cv2
import os
import sys

# ---------- CONFIGURE THIS ----------
# Full path to your image (you already gave this)
image_path = r"C:\Users\Ananya\OneDrive\Documents\pictures\LONDON4.jpg"

# ------------------------------------

def get_int_percent(prompt="Enter blur percentage (0-100): "):
    try:
        p = input(prompt).strip()
        # allow empty to mean 0
        if p == "":
            return 0
        p_int = int(float(p))
        if p_int < 0:
            p_int = 0
        if p_int > 100:
            p_int = 100
        return p_int
    except Exception:
        print("Please enter a number between 0 and 100.")
        return get_int_percent(prompt)

def percent_to_kernel(percent):
    """
    Convert percent (0-100) to a kernel size for GaussianBlur.
    We keep it simple: kernel = percent (min 1). Kernel must be odd.
    If percent == 0 -> no blur (kernel 1 -> effectively original).
    """
    k = max(1, int(percent))
    if k % 2 == 0:
        k += 1
    return k

def main():
    # Load image
    img = cv2.imread(image_path)
    if img is None:
        print(f"Image not found at:\n{image_path}\nMake sure the path and filename are correct.")
        sys.exit(1)

    percent = get_int_percent()
    kernel = percent_to_kernel(percent)

    if percent == 0:
        blurred = img.copy()
        print("0% selected — image left unchanged.")
    else:
        blurred = cv2.GaussianBlur(img, (kernel, kernel), 0)
        print(f"Applied Gaussian blur with kernel size ({kernel},{kernel}) for {percent}% input.")

    # Show image (press any key while image window is focused to close)
    window_name = f"Blurred {percent}%"
    cv2.imshow(window_name, blurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save output next to input image
    folder = os.path.dirname(image_path)
    base = os.path.splitext(os.path.basename(image_path))[0]
    out_name = f"{base}_blur_{percent}.jpg"
    out_path = os.path.join(folder, out_name)
    cv2.imwrite(out_path, blurred)
    print(f"Saved blurred image to: {out_path}")

if __name__ == "__main__":
    main()
