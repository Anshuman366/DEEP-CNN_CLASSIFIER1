FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install -r prediction_service/requirements.txt
CMD ["streamlit", "run", "app.py"]

# we will use python 3.8 slim version
# my working directory is app
# copy everything from local into my working dirctory(copy . .)
# and run the command pip install -r requirements.txt
# and the first command the u will run when we run this file on cmd is   CMD ["streamlit", "run", "app.py"]