# Tahmin Oyunu

Bu Ruby uygulaması, kullanıcının bir sayıyı tahmin etmesine dayanan basit bir oyun sunar. Oyun, kullanıcının her doğru tahmin ettiği sayı için seviye atlamasına olanak tanır.

## Nasıl Oynanır?

- Oyuncu, 1 ile 10 arasında rastgele bir sayıyı tahmin etmeye başlar.
- Tahmin yanlış ise, oyuncu gizli sayının daha büyük veya daha küçük olduğunu söyleyen bir ipucu alır.
- Her seviyede, gizli sayının aralığı artar.
- Oyuncu, her seviyede 3 tahmin hakkına sahiptir.
- Her doğru tahmin edilen sayı için, oyuncu bir sonraki seviyeye geçer ve tahmin hakkı 3'e resetlenir.

## Kurulum

1. Bu projeyi bilgisayarınıza kopyalayın.
2. Terminali açın ve proje dizinine gidin.
3. `ruby guessing_game.rb` komutunu çalıştırın.

## Nasıl Oynanır?

- Oyuncu, 1 ile 10 arasında rastgele bir sayıyı tahmin etmeye başlar.
- Tahmin yanlış ise, oyuncu gizli sayının daha büyük veya daha küçük olduğunu söyleyen bir ipucu alır.
- Her seviyede, gizli sayının aralığı artar.
- Oyuncu, her seviyede 3 tahmin hakkına sahiptir.
- Her doğru tahmin edilen sayı için, oyuncu bir sonraki seviyeye geçer ve tahmin hakkı 3'e resetlenir.

## Örnek Oyun

```txt
Guess a number between 1 and 10 (3 guesses left, level 1): 5
The number is lower than 5.
Guess a number between 1 and 4 (2 guesses left, level 1): 2
Congratulations, you guessed the number in 2 guesses! Moving to level 2...
Guess a number between 1 and 20 (3 guesses left, level 2): 10
The number is higher than 10.
Hint: The number is between 11 and 20
Guess a number between 11 and 20 (2 guesses left, level 2): 15
The number is higher than 15.
Hint: The number is between 16 and 20
Guess a number between 16 and 20 (1 guesses left, level 2): 19
Congratulations, you guessed the number in 3 guesses! Moving to level 3...
Guess a number between 1 and 30 (3 guesses left, level 3): 15
The number is higher than 15.
Hint: The number is between 16 and 30
Guess a number between 16 and 30 (2 guesses left, level 3): 25
The number is lower than 25.
Hint: The number is between 16 and 24
Guess a number
```