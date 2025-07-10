from flask import Flask, request, jsonify
import fitz
import base64
import io

app = Flask(__name__)

@app.route("/")
def index():
    return "PDF Cropper API is running."

@app.route("/crop-to-a6", methods=["POST"])
def crop_to_a6():
    data = request.get_json()
    pdf_b64 = data.get("pdfBase64")
    if not pdf_b64:
        return jsonify({"error": "No PDF data provided."}), 400

    try:
        pdf_bytes = base64.b64decode(pdf_b64)
        doc = fitz.open(stream=pdf_bytes, filetype="pdf")

        # Wymiar etykiety: 100 mm x 150 mm = 283 x 425 pt
        label_width = 283
        label_height = 425

        # Marginesy
        offset_x = 20  # przesunięcie od lewej
        offset_y = 0  # przesunięcie od góry

        for page in doc:
            cropbox = fitz.Rect(
                offset_x,
                offset_y,
                offset_x + label_width,
                offset_y + label_height    
            )
            page.set_cropbox(cropbox)

        output = io.BytesIO()
        doc.save(output)
        output.seek(0)
        cropped_b64 = base64.b64encode(output.read()).decode("utf-8")

        return jsonify({"pdfBase64": cropped_b64})

    except Exception as e:
        return jsonify({"error": str(e)}), 500
