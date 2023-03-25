import 'package:flutter/material.dart';

/// A `ListView.builder` funciona como um construtor em que lhes dá o material que
/// ele deve construir quando necessário. Podes fazer um jogo com o index, como
/// aqui tens, em que entre cada `ListTile` tens uma divisória, `Divider`. A lista
/// torna-se infindável caso não lhe des a propriedade `itemCount`, sendo que aí
/// só construirá o número de items que especificares aí.
///
/// Recomendo veres a documentação em cada widget para perceberes o que cada peça
/// faz neste caso, especialmente teres mais habilidade na `ListView` e na
/// `ListTile`.
class InfiniteList extends StatelessWidget {
  const InfiniteList({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Lista Infinita',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Lista Infinita'),
        ),
        body: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 24.0),
          child: ListView.builder(itemBuilder: (BuildContext ctx, int index) {
            return index % 2 == 0
                ? ListTile(
                    title: Center(
                      child: Text("ListTile #${index / 2}"),
                    ),
                  )
                : const Divider(thickness: 2);
          }),
        ),
      ),
    );
  }
}
