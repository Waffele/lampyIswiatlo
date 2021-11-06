ścieżka do volumes: \\wsl$\docker-desktop-data\version-pack-data\community\docker\volumes

1.odpal docker-compose
2.wyłącz kontenery
3.skopiuj lampyiswiatlo_shop do docker\volumes
4.skopiuj lampyiswiatlo_db\_data\prestashop do docker\volumes

Wyświetlenie kontenerów

    docker ps

Zapisywanie obrazu

    docker commit [3 znaki id] [nazwa obrazu]
    np docker commit 675 lampyiswiatlo-my-prestashop

    docker lasve lampyiswiatlo-my-prestashop > [nazwa pliku]

Wczytywanie obrazu  

    docker load < [nazwapliku]

Kopiowanie plików kontenera

    docker cp [options] [3 znaki id]:/var/www/html [sciezka docelowa]
    np. docker cp 675:/var/www/html ./lampyiswiatlo_shop 
    np. docker cp b15:/var/lib/mysql ./lampyiswiatlo_db                                                                                                                  
