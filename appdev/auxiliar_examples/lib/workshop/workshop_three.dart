import 'package:flutter/material.dart';

/// A app que foi visionada para a parte prática do Workshop. A mesma constitui
/// alguns botões no centro do ecrã e que cada um ativa uma `SnackBar` com uma
/// cor e mensagem personalizada. A fim de conseguir ativar as snackares, as
/// mesmas têm que ser chamadas num widget/class que esteja depois contida num
/// `Scaffold` (neste caso, têm-se que o `Home`, o widget em questão, está
/// dentro do scaffold do `WorkshopThree`).
///
/// Posteriormente, para facilitar a construção de widgets semelhantes (e
/// evitar o copy-paste), criou-se um terceiro widget, `ButtonSnackbar`,
/// onde representa o `ElevatedButton`, com um `Padding` de 10 à volta
/// associado, que mostra a snackbar quando é pressionado. Este novo terceiro
/// widget, tem que ser construido a partir de um texto para mostrar no botão,
/// o parâmetro `txt`, de um texto para mostrar na snackbar, o parâmetro
/// `textSnackbar`, e opcionalmente pode ser especificado uma cor da snackbar,
/// `backgroundSnackbarColor`, que tem como vermelho a cor default.
class WorkshopThree extends StatelessWidget {
  const WorkshopThree({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'HS Template',
      theme: ThemeData(primarySwatch: Colors.green),
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Material App Bar'),
        ),
        body: const Home(),
      ),
    );
  }
}

class Home extends StatelessWidget {
  const Home({super.key});

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: [
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
                  content: Center(
                    child: Text("Olá!"),
                  ),
                  backgroundColor: Colors.red,
                ));
              },
              child: const Text("Primeiro Botão"),
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: ElevatedButton(
              onPressed: () {
                ScaffoldMessenger.of(context).showSnackBar(const SnackBar(
                  content: Center(
                    child: Text("Fui carregado!"),
                  ),
                  backgroundColor: Colors.green,
                ));
              },
              child: const Text("Segundo Botão"),
            ),
          ),
          const ButtonSnackbar(
            txt: "Terceiro Botão",
            textSnackbar:
                "Extrair o widget fica mais fácil de ler e modular o código!",
            backgroundSnackbarColor: Colors.green,
          ),
        ],
      ),
    );
  }
}

class ButtonSnackbar extends StatelessWidget {
  const ButtonSnackbar({
    super.key,
    required this.txt,
    required this.textSnackbar,
    this.backgroundSnackbarColor = Colors.green,
  });

  final String txt;
  final Color backgroundSnackbarColor;
  final String textSnackbar;

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.all(10.0),
      child: ElevatedButton(
        onPressed: () {
          ScaffoldMessenger.of(context).showSnackBar(SnackBar(
            content: Center(
              child: Text(textSnackbar),
            ),
            backgroundColor: backgroundSnackbarColor,
          ));
        },
        child: Text(txt),
      ),
    );
  }
}
