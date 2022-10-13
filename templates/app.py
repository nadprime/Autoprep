from unittest import result
import pandas as pd
from fastapi import FastAPI, UploadFile, File, Form
import shutil
import uvicorn
import aiofiles
from typing import List
import json
import PyPDF2


from transformers import pipeline
from summarizer import Summarizer,TransformerSummarizer

classifier = pipeline('sentiment-analysis')
model = TransformerSummarizer(transformer_type="XLNet",transformer_model_key="xlnet-base-cased")

app = FastAPI()

@app.post("/csvsent")
async def csvsentiment(file: UploadFile = File(...)):
    fname = "./raw/"+file.filename 
    async with aiofiles.open(fname, 'wb') as out_file:
        while content := await file.read(1024): 
            await out_file.write(content)
    
    df = pd.read_csv(fname , encoding = 'latin-1')
    result = df.target.apply(classifier)
    
    df['Sentiment'] = [result[i][0]['label'] for i in range(len(result))]
    df['Score'] = [result[i][0]['score'] for i in range(len(result))]
    df = df[['target','Sentiment','Score']]
    df.to_csv('./raw/csv-output.csv', encoding = 'utf-8-sig',index=False)

    return {"result": df.to_json(orient='records')}

# @app.post("/csv")
# async def csvsentiment(file: UploadFile = File(...)):
#     fname = ""
#     with open(f'{file.filename}',"wb") as buffer:
#         fname = file.filename
#         shutil.copyfileobj(file.file, buffer)
    
#     df = pd.read_csv(fname , encoding = 'latin-1')
#     result = df.target.apply(classifier)
    
#     df['Sentiment'] = [result[i][0]['label'] for i in range(len(result))]
#     df['Score'] = [result[i][0]['score'] for i in range(len(result))]
#     df = df[['target','Sentiment','Score']]
#     df.to_csv('output.csv', encoding = 'utf-8-sig',index=False)

#     return {"result": df.to_json(orient='records')}

@app.post("/sentiment/")
async def sentiment(sentence: str = Form()):
    result = classifier(sentence)
    return {"result": {"Sentiment": result[0]['label'], 
                        "Score": result[0]['score']}
                    }

@app.post("/summarize/")
async def summarize(sentence: str = Form()):
    result = ''.join(model(sentence, min_length=60))
    return {"result": result}


@app.post("/pdf-files-summarize")
async def pdf_files_summarize(files: List[UploadFile] = File(...)):
    for file in files:
        destination_file_path = "./raw/"+file.filename
        async with aiofiles.open(destination_file_path, 'wb') as out_file:
            while content := await file.read(1024): 
                await out_file.write(content)

    df = pd.DataFrame(columns=['PDF Text','Summarized'])

    for file in files:
        pdfReader = PyPDF2.PdfFileReader("./raw/"+file.filename)
        count = pdfReader.numPages
        output = ""
        for i in range(count):
            page = pdfReader.getPage(i)
            output += page.extractText()
        df = df.append({'PDF Text': output, 'Summarized': ''.join(model(output, min_length=60))},ignore_index=True)
    df.to_csv('./raw/PDF-Summarized.csv',index=False)
    return {"Result": "PDF-Summarized.csv Saved!!!"}



@app.post("/text-class/")
async def text_class(
    file: UploadFile = File(),
    project_name: str = Form(),
    task_name: str = Form(),
    textual_coloum: str = Form()):
    fname = "./text-classification/"+file.filename 
    with open(f'{fname}',"wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    import subprocess
    call = "python "+ "./text-classification/textclass.py "+file.filename+" "+project_name+" "+task_name+" "+textual_coloum

    subprocess.Popen(["start", "cmd", "/k", call], shell = True)

    return {
        "MLOps Deployed!!!!!"
    }
#     fname = "./text-classification/"+file.filename 
#     with open(f'{fname}',"wb") as buffer:
#         shutil.copyfileobj(file.file, buffer)


# @app.post("/img")
# async def upload_image(files: List[UploadFile] = File(...)):
# 		for img in files:
# 			with open(f'{img.filename}',"ab") as buffer:
# 				shutil.copyfileobj(img.file, buffer)
# 		return{'file_name':"Good"}


if __name__ == '__main__':
    uvicorn.run(app)
