# BREXIT-APPLICATION

The application analyses the sentiment of tweets with the hashtag "brexit". The crucial step is an appropriate encoding of the sentences. The encoder is taken from facebookresearch. Please see the reference below. Once the encoder has produced sentence embeddings a simple log. regression predicts the sentiment of any given tweet. Accuracy is at about 75%. Could potentially be much higher with a better but mainly larger labelled dataset.

FACEBOOK RESEARCH Sentence Encoder that is used to produce sentence embeddings:

### Supervised Learning of Universal Sentence Representations from Natural Language Inference Data (EMNLP 2017, Outstanding Paper Award)

A. Conneau, D. Kiela, H. Schwenk, L. Barrault, A. Bordes, [*Supervised Learning of Universal Sentence Representations from Natural Language Inference Data*](https://arxiv.org/abs/1705.02364)

```
@article{conneau2017supervised,
  title={Supervised Learning of Universal Sentence Representations from Natural Language Inference Data},
  author={Conneau, Alexis and Kiela, Douwe and Schwenk, Holger and Barrault, Loic and Bordes, Antoine},
  journal={arXiv preprint arXiv:1705.02364},
  year={2017}
}
```

Contact: [aconneau@fb.com](mailto:aconneau@fb.com)
