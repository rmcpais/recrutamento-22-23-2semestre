## Workshop de AppDev

Boas! Aqui podes encontrar material do workshop de AppDev, em Flutter, e para o projeto, bem como informações do mesmo.

Em primeiro lugar, o projeto é para ser entregue duas semanas depois do workshop, 27 de março. 
Isto é, o projeto é para ser entregue a **10 de abril de 2023**!
(se ainda quiseres, às 23h59, horário do fénix) 
Se não conseguires ou tiveres algum problema com o mesmo, por favor, não hesites em mandar mensagem e/ou contactares-me o mais cedo possível! 
A minha tag de discord é `MaxxVilp#5243`, tentarei ser breve a responder.

> Quero reforçar o ponto de comunicação, qualquer coisa, não hesites em mandar mensagem! 
> Desde que seja atempadamente e não em cima da entrega. Não prometo milagres nem ajudar a escrever código.

### Workshop
Os slides do workshop pode ser visto [aqui](https://docs.google.com/presentation/d/1VM8eMKqtHkzsTgK0mAQn3q6KIl_WglAG_23pYutiTN8/edit?usp=sharing).

A parte prática é feita a partir do clone [deste](https://github.com/filipe-varela/hs_appdev_template) repositório, a fim de facilitar o começo de cada participante durante a sessão.
O exemplo criado nesta parte será disponibilizado no `auxiliar_examples/`, como *Workshop 3*, depois do workshop se efetuar.

### Projeto de AppDev
#### Tema
O projeto em si é simples: fazer uma app que tenha uma funcionalidade. 
E pode ser qualquer funcionalidade, por mais simples que esta seja.
Exemplos poderiam ser: 
- Uma to-do list
- Lista de compras
- Um *tracker* de álbuns ou filmes favoritos
- Um *expense tracker*
- Uma app do clima
- E por aí fora...

Desde que tenha pelo menos uma funcionalidade, isso já basta.

#### Requerimentos
Estes requerimentos servem mais como base de apoio, do que regras.
A ideia aqui seria ires dando *check* para poderes dizer que tens o projeto "acabado".

Adicionalmente, estes requerimentos têm que funcionar, pelo menos, para a plataforma que estiveres a programar.
Pode ser a mesma que do workshop, web, como móvel ou de computador.
Desde que funcione na plataforma que estejas a programar, isso basta! 

Pondo isto, tens o seguinte:
1. App que é app, precisa de um [splash screen](https://pub.dev/packages/flutter_native_splash). 
Tenta implementar um e personalizá-lo!
2. Pelo menos ter mais que uma página para o(a) utilizador(a) possa navegar.
Há inúmeras maneiras de concretizar este passo, sendo que uma delas que recomendo é [esta](https://docs.flutter.dev/cookbook/navigation/navigation-basics).
3. De certa maneira, consiga [persistir os dados](https://pub.dev/packages/shared_preferences) entre sessões - uma sessão é definida como o período entre o abrir e o fechar da aplicação.
Cabe a ti dizer que dado deva ser persistido - pode ser o nome de alguém ou as vezes que visitou a aplicação por exemplo, desde que seja persistido é o que conta.

Claro que será mais interessante poderes fazer mais funcionalidades do que estas aqui mostradas, mas isso será ao teu dispor.
Os três pontos serão considerado como os mínimos.

### Entrega
A entrega em si tem que conter dois materiais:
1. O código em si, como em qualquer outro projeto de programação feito anteriormente no recrutamento.
2. Dentro da pasta do vosso projeto, tem de estar uma pasta adicional a dizer `final`. 
Dentro desta pasta, queria ver a versão final da aplicação, aquela que resulta do `flutter build <plataforma> --release` (caso tenhas feito uma aplicação web, terias de escrever `flutter build web --release`; caso fosse android, `flutter build apk --release` e por aí fora). 
Assim, é possível testar o teu código sem necessitar de compilar o teu projeto localmente. **Atenção:** o resultado do `flutter build` vai dar à pasta `build`, por isso, move os ficheiros que queres entregar dessa pasta para a `final` por favor!

Tudo isto dentro da pasta `Entregas`!

> Atenção numa particularidade relativamente à entrega, é melhor criares a pasta com os teus `PrimeiroÚltimo` nomes e depois lá dentro fazes `flutter create <nome do projeto>`. 
> Não faças `flutter create .`, dado que a pasta não tem a convenção indicada pela equipa de desenvolvimento do Flutter e, também, teria mais piada se deres nome próprio à tua app, não é verdade?

### Palavras finais
Não precisas de te preocupar mais, a informação para o projeto em si já foi dita!
Esta secção está aqui para dar mais recursos de apoio caso queiras.

Primeiro lugar, consegues encontrar nesta pasta uma subdiretoria chamada `auxiliar_examples`.
Nela, tens alguns exemplos de funcionalidades simples que consegui fazer numa tarde e meia e que achei que pudesse ser útil para os projetos ou para mostrar os diferentes widgets que podes usar. 
A maneira como ela está estruturada está explicado no respetivo `README.md`.

Em segundo lugar, tens a seguinte lista links que penso que possam ajudar caso queiras mais guia e mais materiais do que aqueles que consegui dar:
- [Tutoriais](https://docs.flutter.dev/reference/tutorials) e [Codelabs](https://docs.flutter.dev/codelabs) da equipa de desenvolvimento de Flutter, explicam alguns conceitos básicos;
- [Widget of the week](https://youtube.com/playlist?list=PLjxrf2q8roU23XGwz3Km7sQZFTdB996iG) - para o caso de quereres explorar melhor os widgets que existem;
- [Crash course para iniciantes](https://youtu.be/x0uinJvhNxI); (5h42min)
- [Flutter Crash Course](https://youtu.be/1gDhl4leEzA); (59min)
- [Documentação do flutter](https://docs.flutter.dev/) - apesar de normalmente não se ver a documentação, eu recomendo porque tens, por norma, um exemplo iterativo associado para poderes testar o widget que estiveres a ver. 
Recomendo vivamente mesmo!
- [Flutter favorite packages](https://pub.dev/packages?q=is%3Aflutter-favorite) - packages recomendados.

### Extensões que recomendo
Para VSCode, eu uso as seguintes extensões:
- As extensões próprias para [Dart](https://marketplace.visualstudio.com/items?itemName=Dart-Code.dart-code) e [Flutter](https://marketplace.visualstudio.com/items?itemName=Dart-Code.flutter)
- [Awesome Flutter Snippets](https://marketplace.visualstudio.com/items?itemName=Nash.awesome-flutter-snippets): Ajuda nas sugestões e no refactor
- [Flutter Widget Snippets](https://marketplace.visualstudio.com/items?itemName=alexisvt.flutter-snippets): Ajuda nas sugestões e no refactor
- [CSS Flutter Colors](https://marketplace.visualstudio.com/items?itemName=circlecodesolution.ccs-flutter-color): Ajuda a ver e modificar as cores no Flutter
- Caso não tenhas, procura por Rainbow Brackets (no VSCode já é um built-in, não sei para as outras plataformas)
- (Opcional) [Live Share](https://marketplace.visualstudio.com/items?itemName=MS-vsliveshare.vsliveshare) Para partilhar e ser mais fácil de ver o código entre computadores

Para outras plataformas, recomendo ires ver se consegues extensões que te ajudem nas sugestões e nas cores, visto que isso é o que vais mexer mais no projeto, em principio!

---

De resto é isto! 
Boa sorte com o projeto e, mais uma vez (que não são vezes a mais), se tiveres algum problema, por favor, manda mensagem a `MaxxVilp#5243` no discord. 

Good hacking!