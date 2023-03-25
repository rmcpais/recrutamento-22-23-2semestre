import 'package:flutter/material.dart';

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
