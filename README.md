# Intro to spatial and non Spatial Queries

<p>
  <a href="https://twitter.com/AlphaOmondi" target="_blank">
    <img alt="Twitter: AlphaOmondi" src="https://img.shields.io/twitter/follow/AlphaOmondi.svg?style=social" />
  </a>
</p>

👋 Intro series on Spatial querying with Geodjango and Django REST Framework.

## Run the Application

```
git clone https://github.com/API-Imperfect/geodjango-hospitals-api
cd geodjango-hospitals-api
 - run the command: make build
 - run the migrate command: make migrate
 - create superuser: make superuser
 - then run the command: make shell
to load hospital data run these commands in the shell
>>> from hospitals import load
>>> load.run()

to load boundaries data run these commands
>>> from boundaries import load
>>> load.run()
>>> quit()

🏃🏽‍♂️ API Requests
Open Postman and make the following get requests
GET http://localhost:8080/api/v1/hospitals/
GET http://localhost:8080/api/v1/boundaries/
GET http://localhost:8080/api/v1/hospitals/?province=1
GET http://localhost:8080/api/v1/hospitals/closest_hospitals/?lon=30.094388&lat=-1.943566
GET http://localhost:8080/api/v1/hospitals/total_bed_capacity/
GET http://localhost:8080/api/v1/hospitals/province_beds_capacity/

```

## License

MIT
