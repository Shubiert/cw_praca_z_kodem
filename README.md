# cw_praca_z_kodem

CI/CD to skrót od Continuous Integration (CI) i Continuous Deployment (CD).
Jest to zestaw praktyk i narzędzi stosowanych w procesie rozwoju oprogramowania,
które mają na celu automatyzację budowy, testowania i wdrażania aplikacji.

Continuous Integration (CI) to praktyka polegająca na częstym i automatycznym integrowaniu kodu źródłowego zespołu programistycznego w wspólnym repozytorium.
Głównym celem CI jest zapewnienie, że wszyscy programiści w zespole regularnie wprowadzają swoje zmiany i integrują je z istniejącym kodem. 
Dzięki temu można szybko wykrywać i rozwiązywać konflikty, błędy czy problemy z integracją, zanim zostaną wprowadzone do głównego systemu.

Continuous Deployment (CD) to natomiast praktyka polegająca na automatycznym wdrażaniu zmian w kodzie, które zostały zintegrowane przy użyciu CI.
Oznacza to, że każda zatwierdzona zmiana jest automatycznie budowana, testowana i wdrażana do środowiska produkcyjnego lub innego docelowego środowiska.
Dzięki CD można skrócić czas między wprowadzeniem zmiany a jej dostępnością dla użytkowników, co z kolei przyspiesza tempo rozwoju i umożliwia szybką 
reakcję na zmieniające się wymagania.

W połączeniu CI/CD umożliwiają automatyczne i powtarzalne budowanie, testowanie i wdrażanie aplikacji, 
co prowadzi do zwiększenia jakości oprogramowania, skrócenia cyklu dostarczania i większej efektywności zespołu.
Narzędzia takie jak Travis CI są często wykorzystywane do automatyzacji tych procesów, umożliwiając programistom 
pracę w sposób bardziej płynny i produktywny.


Docker to otwarte oprogramowanie, które umożliwia wirtualizację na poziomie systemu operacyjnego. Jest to platforma, 
która umożliwia tworzenie, wdrażanie i uruchamianie aplikacji w izolowanych kontenerach. Kontenery Dockerowe są lekkie, 
przenośne i mają możliwość replikacji w różnych środowiskach, co czyni je popularnym narzędziem w dziedzinie wdrażania oprogramowania.

Docker wykorzystuje obrazy, które są swoistymi szablonami do uruchamiania kontenerów. Obraz Dockerowy zawiera wszystkie 
zależności i komponenty potrzebne do uruchomienia aplikacji. Dzięki temu można zapewnić, że aplikacja będzie działać w dokładnie 
takim samym środowisku, niezależnie od systemu operacyjnego czy konfiguracji hosta.

Składnia i pliki konfiguracyjne używane w Dockerze są opisane w pliku o nazwie "Dockerfile". Poniżej znajduje się krótkie omówienie
najważniejszych elementów składni i plików konfiguracyjnych Dockerfile:

Dyrektywa "FROM": Określa obraz bazowy, na którym zostanie zbudowany nowy obraz. Na przykład, można użyć obrazu "ubuntu" jako podstawy dla swojego obrazu.

Dyrektywa "RUN": Wykonuje określone polecenie w kontekście budowy obrazu. Można użyć go do instalacji oprogramowania, aktualizacji pakietów, skonfigurowania środowiska itp.

Dyrektywa "COPY" lub "ADD": Kopiuje pliki z lokalnego systemu do obrazu. Można użyć jej do dodawania kodu źródłowego aplikacji do obrazu.

Dyrektywa "EXPOSE": Deklaruje porty, na których aplikacja wewnątrz kontenera nasłuchuje po uruchomieniu.

Dyrektywa "CMD" lub "ENTRYPOINT": Określa polecenie, które zostanie wykonane po uruchomieniu kontenera. Może to być komenda uruchamiająca serwer aplikacji.

Po napisaniu pliku Dockerfile, można użyć komendy "docker build" w celu zbudowania obrazu na podstawie tego pliku. 
Obraz można następnie uruchomić przy użyciu komendy "docker run", podając odpowiednie opcje, takie jak mapowanie portów czy wolumeny.

Dodatkowo, Docker udostępnia wiele narzędzi i funkcji, takich jak Docker Compose (do zarządzania wieloma kontenerami jako pojedynczą aplikacją), 
Docker Swarm (do zarządzania klastrami kontenerów) czy Docker Registry (do przechowywania i udostępniania obrazów).

Docker jest bardzo popularny wśród deweloperów i inżynierów DevOps, ponieważ ułatwia wdrażanie aplikacji w izolowanych kontenerach, 
co przyspiesza cykl dostarczania i zapewnia spójne środowisko dla aplikacji na różnych platformach.




