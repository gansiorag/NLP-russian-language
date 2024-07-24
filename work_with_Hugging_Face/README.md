### Введение в библиотеку Transformers и платформу Hugging Face

Исходники: https://github.com/huggingface/transformers <br>
Документация: https://huggingface.co/docs/transformers/main/en/index

Платформа Hugging Face это коллекция готовых современных предварительно обученных Deep Learning моделей. А библиотека Transformers предоставляет инструменты и интерфейсы для их простой загрузки и использования. Это позволяет вам экономить время и ресурсы, необходимые для обучения моделей с нуля.

Модели решают весьма разнообразный спектр задач:

    NLP: classification, NER, question answering, language modeling, summarization, translation, multiple choice, text generation.

    CV: classification, object detection,segmentation.

    Audio: classification, automatic speech recognition.

    Multimodal: table question answering, optical character recognition, information extraction from scanned documents, video classification, visual question answering.

    Reinforcement Learning

    Time Series

Одна и та же задача может решаться различными архитектурами и их список впечатляет - более 150 на текущий момент. Из наиболее известных: Vision Transformer (ViT), T5, ResNet, BERT, GPT2. На этих архитектурах обучены более ат 31/05/2024 - 198 888 моделей.

Transformers не является набором модулей, из которых составляется нейронная сеть, как например PyTorch. Вместо это Transformers предоставляет несколько высокоуровневых абстракций, которые позволяют работать с моделями в несколько строк кода.

### Установка

Нам понадобится сами трансформеры:

#### pip install transformers

И т.к. мы будем писать на торче, то:

#### pip install torch

Еще нам понадобится библиотека evaluate, которая предоставляет различные ML метрики:

#### pip install evaluate

Поиск моделей

Прежде чем приступать к коду нам нужно формализовать нашу задачу до одного из общепринятых классов и найти подходящую для нее модель на хабе Hugging Face: https://huggingface.co/models