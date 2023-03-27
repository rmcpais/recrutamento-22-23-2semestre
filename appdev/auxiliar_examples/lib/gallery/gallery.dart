import 'package:flutter/material.dart';

import 'package:auxiliar_examples/gallery/gallery_exposition.dart';

class Gallery extends StatelessWidget {
  const Gallery({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Galeria moderna',
      home: Scaffold(
        appBar: AppBar(
          title: const Text('Galeria moderna'),
        ),
        body: const GalleryExposition(),
      ),
    );
  }
}
