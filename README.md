# Projeto Final
Projeto Final - Graduação Engenharia de Computação UERJ

## Teste Inicial 
Este teste inicial foi feito de acordo com este [vídeo](https://www.youtube.com/watch?v=mCcPmlr7y3U&t=511s). Com a utilização das bibliotecas [OpenCV](https://pypi.org/project/opencv-python/) e [MediaPipe](https://google.github.io/mediapipe/).

### OpenCV
Biblioteca multiplataforma que possui módulos para processamento de imagens e vídeos, álgebra linear, estrtutura de dados, interface gráfica do usuário, etc. Possui algoritmos que auxiliam na calibração de câmera, reconhecimento de objetos, análise estrutural e filtro ed imagens. Esta biblioteca foi desenvolvida em C/C++, porém possui suporte à linguagens como Java e Python.

```
pip install opencv-python
```

### Mediapipe
Framework da Google utilizado para construção de pipelines de aprendizado de máquina para o processamento de dados relacionados a áudio, vídeo, etc. Este framework foi desenvolvido em C++, JAVA e Obj-C, e sua estrutura consiste em 3 principais APIs:
- API de Calculadora
- API de construção de gráficos
- API de execução de gráficos

O MediaPipe possui modelos de código aberto, ou seja, soluções já feitas por outras pessoas que podem ser usadas pela comunidade. Estas são feitas em um modelo de TensorFLow ou TFLite pré-treinado de acordo com o caso específico. Neste caso, utilizaremos a solução que aborda a detecção de rosto.

```
pip install mediapipe
```
