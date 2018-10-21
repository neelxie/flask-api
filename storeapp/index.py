from flask_restful import Resource

message = """
       <!DOCTYPE html>
     <html>
       <head>
         <title>Store Manager Flask API</title>
         <style type='text/css'>
           *{
               margin:0;
               padding:0;
           }
           body{
               width:80%;
               margin:0 auto;
           }
           .main-container{
               margin-top:45px;
           }
           h2{
               font-size:16pt;
               color:orange;
               text-align:center;
           }
           a{
               text-decoration:none;
           }
         </style>
       </head>
       <body>
         <div class='main-content'>
           <h2>Store Manager Flask Api</h2>
              Currently supported endpoints <br>
              <a href='https://warm-mountain-24705.herokuapp.com/storemanager/api/v1/Products'>Products</a> <br/>
              <a href='https://warm-mountain-24705.herokuapp.com/storemanager/api/v1/Sales'>Sales</a>
         </div>
       </body>
     </html>
"""
class Index(Resource):
    def get(self):
        return message