# PDF Cropper API (A6)

Simple Flask API that accepts a base64-encoded PDF and returns a cropped A6 version (from bottom-right corner).

## Endpoint

- `POST /crop-to-a6`
- JSON body: `{ "pdfBase64": "<...>" }`
- Returns: `{ "pdfBase64": "<cropped version>" }`

## Deployment

Ready to deploy on [Render.com](https://render.com) as a "Web Service".