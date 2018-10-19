rent-price-converter
=================

![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)
 [![Tweet](https://img.shields.io/twitter/url/http/shields.io.svg?style=social)](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Fnejckorasa%2Frent-price-converter&via=nejckorasa&text=Awesome%20Rent%20Price%20Converter&hashtags=rentpriceconverter%2C%20apartments%2C%20rent%2C%20development%2C%20programming%2C%20github%2C%20python%2C%20software)


What is it
-------

Ever looked for apartments to rent and had problems converting between **PW** (per week) and **PCM** (per calendar month) rent prices? 

Maybe it's just me... Anyway, here's a Python script to help you with conversion.

Use responsibly.

Conversion Function
-------

```
rent_pw * 52 / 12 = rent_pcm

# For example
150 pw * 52 / 12 = 650 pcm
```

Usage
-------

```
> ./rent_conversion.py 1300 pcm
300 pw
```

```
> ./rent_conversion.py 150 pw
650 pcm
```

