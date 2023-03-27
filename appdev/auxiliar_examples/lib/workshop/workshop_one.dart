import 'package:flutter/material.dart';

void main() {
  runApp(MaterialApp(
    title: "Flutter Demo",
    theme: ThemeData(
      primaryColor: Colors.teal,
      visualDensity: VisualDensity.adaptivePlatformDensity,
    ),
    home: Scaffold(
      appBar: AppBar(
        title: const Text("Starter App"),
      ),
      body: const Center(
        child: Text("Hello World"),
      ),
    ),
  ));
}
