```mermaid
  sequenceDiagram
  
  main->>laitehallinto: HKLLaitehallinto()
  main->>rautatietori: Lataajalaite()
  main->>ratikka6: Lukijaliate()
  main->>bussi224: Lukijaliate()
  main->>laitehallinto: lisaa_lataaja(rautatietori)
  main->>laitehallinto: lisaa_lukija(rattika6)
  main->>laitehallinto: lisaa_lukija(bussi224)
  main->>lippu_luuku: Kioski()
  main->>lippu_luuku: osta_matkakortti("Kalle")

  lippu_luuku->>kallen_kortti: Matkakortti(Kalle)
  main->>rautatietori: lataa_arvoa(kallen_kortti, 3)
  rautatietori->>+kallen_kortti(kasvata_arvoa, 3)
  deactivate kallen_kortti
  main->>+rattika6: osta_lippu(kallen_kortti, 0)

  ratikka6->>+kallen_kortti: kortti.arvo
  kallen_kortti-->>-ratikka6: 3
  ratikka6->>+kallen_kortti: vahenna_arvoa(1.5)
  deactivate kallen_kortti
  ratikka6-->>-main: True
  main->>+bussi244: osta_lippu(kallen_kortti, 2)

  bussi244->>+kallen_kortti: kortti.arvo
  kallen_kortti-->>-bussi244: 1.5
  bussi244-->>-main: False


```
