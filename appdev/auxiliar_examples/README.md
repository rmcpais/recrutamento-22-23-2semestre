## Exemplos auxiliares
Este mini-projeto mostra algumas funcionalidades possíveis com o flutter. 
Não é exaustivo, mas consegue dar uma ideia das coisas que se possam fazer a framework.

### Exemplos
Os exemplos aqui mostrados são os seguintes:
- **Default**: O exemplo default do flutter, um que seja gerado automaticamente pelo comando `flutter create <nome_do_projeto>` por exemplo. 
Está guardado num único ficheiro e foi deixado para o caso de se querer verificar como é que é o resultado proveniente do default. 
Este exemplo apresenta um `Floating Action Button`, `Stateful` e `Stateless` widgets, `Center` e `Column` para organização.
Está bem organizado e documentado, por isso, deixo para dar mais valor aos restantes exemplos (que são mais simples por comparação);
- **Menu**: Um exemplo simples de como fazer um *menu*.
Este menu apenas contem `Elevated Button`s para poder guiar o utilizador da página principal para uma secundária, onde mostra a cor que o utilizador escolheu.
Claro que o design poderia estar melhor, mas o propósito aqui era de mostrar como criar um menu e como se pode guiar o utilizador de uma página para outra.
Para além disso, há uma explicação no topo do ficheiro principal (aquele que tem o mesmo nome que a pasta) para poder ir mais ao detalhe como está montado.
- **Infinite List**: Como o nome indica, é um exemplo de como se pode implementar uma *lista infinita* no flutter.
No ficheiro principal tem-se a explicação de como isto é possível, sendo que os elementos mais importantes é teres uma `ListView.builder` e um widget que sirva para preencher a lista - para este tipo de casos, é normalmente usado `ListTile`.
Em termos de conteúdo, poderia ter conteúdo mais importante, mas neste caso deixou-se que cada elemento da lista tivesse um formato `ListTile #<numero do item>` para simplificar a demonstração.
- **Gallery**: Numa forma mais interessante e iterativa que os exemplos anteriores, este demo mostra como criar uma galeria de imagens proveniente de uma API e permite ao utilizador escolher uma das imagens para ser a que estiver no meio da página.
Esta combina um pouco da **Infinite List** com a implementação do widget `Image.network`, a fim de mostrar as imagens, bem como usar o `InkWell` para adicionar a propriedade de *click* na imagem, quando se quer adicioná-la. 
Este exemplo é bastante simples no papel, mas pode ser desafiante a quem ainda não perceber os exemplos anteriores;
- **Workshop 2**: A app que se usou como exemplo para o workshop.
- **Workshop 3**: A app que se usou como exemplo prático para o workshop.

Por enquanto são estes o exemplos adicionados, sendo que será avisado quando forem adicionados mais exemplos.

> Nota! Estes exemplos não seguem a 100% as boas práticas, sendo que deves ver isto como `como implementar certa funcionalidade` e não como se escreve bom código. 
> Entre outras palavras, está por tua conta e risco se fizeres copy-paste e não funcionar

Para poderes escolher o exemplo, tens de ir ao `lib/main.dart` e alterar o `exemploId` para uma das opções que terás em baixo. 
Caso queiras o `default`, basta colocares um nome qualquer, desde que não seja igual aos que estão alistados.
