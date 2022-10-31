## Back-End Lab1

- Setting up a development environment.
- RESTful API development.

`Anna Kramar, group: IK-02`

### Tests on Postman:
- [Collection](https://drive.google.com/file/d/1QVJcblDo30N8ZUdeQUvrfOzRPqSVBgQ9/view?usp=sharing)

- [Local environment](https://drive.google.com/file/d/1LuknbRFC6Bggfp--hjupMexSAgCmvifj/view?usp=sharing)

- [Production environment](https://drive.google.com/file/d/1fGUtEJxmVpVHnaBwlhC-fY0gHDLLxE-g/view?usp=sharing)

### Heroku
- [Heroku App](https://backend-lab1-recipes.herokuapp.com/)

### Python
1. `set FLASK_APP = recipes`
2. `flask run`

### Docker
1. `docker build --build-arg PORT=5000 . -t <image_name>:latest
`
2. `docker-compose build`
3. `docker-compose up`
