
## Comandos

```
python3 -m venv env

.\env\Scripts\activate


# Actualizar el pip

pip show pip
python -m pip install --upgrade pip


# Packages

pip install pylint
pip install autopep8
pip list
```

```
git branch -M main

git remote add origin https://github.com/TomasOtano25/curso-python.git

git push -u origin main
```

## Link

https://htmlcolorcodes.com/es/


# Distribucion y ejecutable

```
env/Scripts/activate

pip install pyinstaller

pyi-makespec catalogo_peliculas.py --windowed

Luego de modificado el .spec:

pyinstaller catalogo_peliculas.spec

```

En nuestro archivo `.spec`:

```
datas=[('./img/*ico', 'img'), ('./database/*.db', 'database')],
```