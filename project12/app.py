from flask import Flask,render_template,request  
import requests

app=Flask(__name__)
API_KEY="triology"

@app.route("/",methods=["GET","POST"])
def home():
  movie=None
  error=None
  if request.method=="POST":
    movie_name=request.form.get("movie_name")

    try:
        url="http://www.omdbapi.com/?apikey={API_KEY}&t{movie_name}"
        response=requests.get(url)
        data=response.json()

        if data.get("Response")=="True":
          movie=data
        else:
         error=f"Movie not found{data.get('Error','Unknown Error')}"

    except Exception as e:
       error=f"Error for fetching data:{str(e)}"
  return render_template("index.html",movie=movie,error=error)

if __name__=='__main__':
  app.run(debug=True)
       

