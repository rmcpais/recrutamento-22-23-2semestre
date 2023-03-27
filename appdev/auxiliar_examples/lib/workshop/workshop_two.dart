import 'package:flutter/material.dart';

class WorkshopTwo extends StatelessWidget {
  const WorkshopTwo({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flutter Demo',
      home: MainScreen(),
    );
  }
}

class MainScreen extends StatefulWidget {
  const MainScreen({super.key});

  @override
  State<MainScreen> createState() => _MainScreenState();
}

class _MainScreenState extends State<MainScreen> {
  int counter = 0;
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Starter App'),
      ),
      body: TextCenter(
        data: "Hello world $counter times",
      ),
      floatingActionButton: FloatingActionButton(
        onPressed: () => setState(() {
          counter++;
        }),
        child: const Icon(Icons.all_inclusive),
      ),
    );
  }
}

class TextCenter extends StatelessWidget {
  const TextCenter({
    super.key,
    required this.data,
    this.scale,
  });

  final String data;
  final double? scale;

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text(data, textScaleFactor: scale),
    );
  }
}
