#!/bin/sh

curl -X POST http://127.0.0.1:8000/predict -H "Content-Type: application/json" -d '{"age":{"0":60,"1":58,"2":56,"3":58},"sex":{"0":0,"1":0,"2":1,"3":1},"cp":{"0":2,"1":0,"2":0,"3":0},"trestbps":{"0":120,"1":100,"2":132,"3":100},"chol":{"0":178,"1":248,"2":184,"3":234},"fbs":{"0":1,"1":0,"2":0,"3":0},"restecg":{"0":1,"1":0,"2":0,"3":1},"thalach":{"0":96,"1":122,"2":105,"3":156},"exang":{"0":0,"1":0,"2":1,"3":0},"oldpeak":{"0":0.0,"1":1.0,"2":2.1,"3":0.1},"slope":{"0":2,"1":1,"2":1,"3":2},"ca":{"0":0,"1":0,"2":1,"3":1},"thal":{"0":2,"1":2,"2":1,"3":3}}'
