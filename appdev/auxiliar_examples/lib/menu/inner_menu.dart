import 'package:flutter/material.dart';

import 'blank_screen.dart';

/// O InnerMenu tem como principal função de mostrar como fazer um menu simples e
/// com séries de botões. O `for` no final é uma forma abreviada de criares uma
/// lista sem teres que fazer muito copy-paste.
/// O `Padding` cria espaço entre os botões, o `Center` centra os widgets ao ecrã
/// e o `Column` organiza os widgets em forma de coluna
class InnerMenu extends StatelessWidget {
  const InnerMenu({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Demo: menu")),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          mainAxisSize: MainAxisSize.max,
          children: [
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: ElevatedButton(
                onPressed: () => Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => const BlankScreen("Red"),
                    )),
                child: const Text("Vermelho"),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: ElevatedButton(
                onPressed: () => Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => const BlankScreen("Blue"),
                    )),
                child: const Text("Azul"),
              ),
            ),
            Padding(
              padding: const EdgeInsets.all(8.0),
              child: ElevatedButton(
                onPressed: () => Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => const BlankScreen("Green"),
                    )),
                child: const Text("Verde"),
              ),
            ),
            for (String otherColors in [
              "Cyan",
              "Orange",
              "Yellow",
              "Orange",
              "Amber"
            ])
              Padding(
                padding: const EdgeInsets.all(8.0),
                child: ElevatedButton(
                  onPressed: () => Navigator.push(
                      context,
                      MaterialPageRoute(
                        builder: (context) => BlankScreen(otherColors),
                      )),
                  child: Text(otherColors),
                ),
              )
          ],
        ),
      ),
    );
  }
}
