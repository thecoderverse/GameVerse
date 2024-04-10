# Hangman | Adam Asmaca

Hangman basit bir terminal oyunudur. Oyuncu dünya klasiklerinden eser ismi Türkce veya İngilizce olacak şekilde seçimini yapar. Sonrasında eserlerin kategorileri içinden istediği kategoriyi seçer ve oyun başlar. 
Oyun Python dilinde yazılmıştır ve aşağıdaki özelliklere sahiptir.

- Kitaplar bir JSON dosyasından okunur.
- Kullanıcı oyuna başlamadan önce kitap isminin dilini ve kategorisini seçer.
- Kullanıcı kitap isminde olmayan bir harf yazdığında darağacı kurulmaya başlar.
- İpucu almak için ? (soru işareti) yazarak harf alabilir.
- Toplam 6 yanlış tahmin sonrası oyun sonlanır ve adam asılmış olur.

## Kullanılan Kütüphaneler

Programda kullanılan kütüphaneler şöyledir;

- json dosyasını parse edip verileri almak için **json** kütüphanesi
- Kitap listesinden rastgele kitap seçimi için **random** kütüphanesi
- Oyun açılışında ki minik animasyon için **time** kütüphanesi

## Çalışma Zamanı

```
python hangman.py
╔═══════════════════════════════════════════════╗
║               Welcome to Hangman              ║
╚═══════════════════════════════════════════════╝
                      ╔═════╗
                      O     ║
                     /|\    ║
                      |     ║
                     / \    ║
                    ════════╝
╔═══════════════════════════════════════════════╗
║         1 - Turkish Books Name                ║
║         2 - English Books Name                ║
║         3 - Exit                              ║
╚═══════════════════════════════════════════════╝
Select > 2
╔═══════════════════════════════════════════════╗
║     1 - Novel               2 - Philosophy    ║
║     3 - Dystopian           4 - Short Story   ║
║     5 - Fantasy             6 - Adventure     ║
║     7 - Novella             8 - Play          ║
╚═══════════════════════════════════════════════╝
Select books category > 1
 _  _  _  _  _    _  _  _  _  _  _  _  _  _  _  _  _ 

You have 6 guesses. If you want hint, you can write [ ? ]

Write your guess letter or word :\> q


  ╔═════╗


 _  _  _  _  _    _  _  _  _  _  _  _  _  _  _  _  _

You have 5 guesses. If you want hint, you can write [ ? ]
You use ['q'] letters

Write your guess letter or word :\> w


  ╔═════╗
  O     ║


 _  _  _  _  _    _  _  _  _  _  _  _  _  _  _  _  _

You have 4 guesses. If you want hint, you can write [ ? ]
You use ['q', 'w'] letters

Write your guess letter or word :\> r


  ╔═════╗
  O     ║


 _ r _  _  _    _  _  _  _  _  _  _  _  _  _  _  _

You have 4 guesses. If you want hint, you can write [ ? ]
You use ['q', 'w', 'r'] letters

Write your guess letter or word :\> t


  ╔═════╗
  O     ║


 _ r _  _ t   _  _  _  _  _ t _ t _  _  _  _

You have 4 guesses. If you want hint, you can write [ ? ]
You use ['q', 'w', 'r', 't'] letters

Write your guess letter or word :\> y


  ╔═════╗
  O     ║
 /|\    ║


 _ r _  _ t   _  _  _  _  _ t _ t _  _  _  _

You have 3 guesses. If you want hint, you can write [ ? ]
You use ['q', 'w', 'r', 't', 'y'] letters

Write your guess letter or word :\> u


  ╔═════╗
  O     ║
 /|\    ║
  |     ║


 _ r _  _ t   _  _  _  _  _ t _ t _  _  _  _

You have 2 guesses. If you want hint, you can write [ ? ]
You use ['q', 'w', 'r', 't', 'y', 'u'] letters

Write your guess letter or word :\> p


  ╔═════╗
  O     ║
 /|\    ║
  |     ║


 _ r _  _ t   _  _ p _  _ t _ t _  _  _  _ 

You have 2 guesses. If you want hint, you can write [ ? ]
You use ['q', 'w', 'r', 't', 'y', 'u', 'p'] letters

Write your guess letter or word :\> l


  ╔═════╗
  O     ║
 /|\    ║
  |     ║
 / \    ║


 _ r _  _ t   _  _ p _  _ t _ t _  _  _  _

You have 1 guesses. If you want hint, you can write [ ? ]
You use ['q', 'w', 'r', 't', 'y', 'u', 'p', 'l'] letters

Write your guess letter or word :\> k


  ╔═════╗
  O     ║
 /|\    ║
  |     ║
 / \    ║
════════╝


You lost. Game over

Your Scores:0 Win, 1 Lost
Would you like to play again? [Y]es / [N]o / [M]ain Menu: n
Thank you!
```

![hangman.png](hangman.png)
