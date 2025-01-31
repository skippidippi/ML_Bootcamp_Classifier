# Baseline_Classifier

Базовое решение, которое описывает подход по реализации сервиса для классификации сообщений, выводится на порт **443**

## Выбор модели классифаера

***Перепробовали несколько вариантов, остановились на модели [facebook/bart-large-mnli](https://huggingface.co/facebook/bart-large-mnli), так как она менее чувствительна к ботам***

## Выбор трешхолда

***Использовали различные трешхолды, например 0.9 и 0.45, даже реверсивный трешхолд, то есть от 0 до 0.3 и от 0.7 до 1 классифицируем как бота, а промежуточные значения как человека. В итоге решили не использовать трешхолд, так как модель справлялась без него***