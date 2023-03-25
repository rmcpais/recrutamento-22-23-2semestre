import 'package:flutter/material.dart';

const Map<String, MaterialColor> str2colors = {
  "red": Colors.red,
  "blue": Colors.blue,
  "green": Colors.green,
  "cyan": Colors.cyan,
  "pink": Colors.pink,
  "orange": Colors.orange,
  "yellow": Colors.yellow
};

/// Simplesmente uma página que esteja preenchida por uma cor, nada de mais.
/// A Appbar permite não só mostrar o nome da cor, como também dar a
/// possibilidade de retornar para a página anterior.
class BlankScreen extends StatelessWidget {
  const BlankScreen(this.color, {super.key});

  final String color;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(color),
      ),
      body: Container(
        color: str2colors[color.toLowerCase()] ?? Colors.amber,
      ),
    );
  }
}
