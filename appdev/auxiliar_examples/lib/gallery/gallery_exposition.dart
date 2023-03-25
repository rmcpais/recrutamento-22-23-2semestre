import 'package:flutter/material.dart';

/// Um exemplo de stateful widget, onde na parte central vais ter uma
/// imagem vinda de url, `Image.network`, e em baixo tens uma galeria
/// de imagens, montada do mesmo estilo que a lista infinita, às quais
/// podes clicar e alterar a que estiver na principal. A particularidade
/// deste widget, sobre o stateless, é que é possível alterar o que
/// te pode aparecer à frente sem teres de montar uma página ou widget
/// diferente. Alteras o link da `Image.network` e pedes para
/// renderizar de novo com a função `setState`. O `Expanded` serve
/// só para poder organizar melhor o layout, fazendo o controlo do
/// mesmo pelo fit.
class GalleryExposition extends StatefulWidget {
  const GalleryExposition({super.key});

  @override
  State<GalleryExposition> createState() => _GalleryExpositionState();
}

class _GalleryExpositionState extends State<GalleryExposition> {
  String currentURL = "https://picsum.photos/250?image=0";
  String templateURL = "https://picsum.photos/250?image=";
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisSize: MainAxisSize.max,
        children: [
          Expanded(
            flex: 7,
            child: Padding(
              padding: const EdgeInsets.symmetric(vertical: 12.0),
              child: Image.network(currentURL, fit: BoxFit.fill),
            ),
          ),
          Expanded(
            flex: 1,
            child: ListView.builder(
              itemCount: 50,
              scrollDirection: Axis.horizontal,
              itemBuilder: (BuildContext ctx, int index) {
                return InkWell(
                  onTap: () {
                    setState(() => currentURL = "$templateURL$index");
                  },
                  child: Image.network(
                    "$templateURL$index",
                    fit: BoxFit.fitHeight,
                  ),
                );
              },
            ),
          ),
        ],
      ),
    );
  }
}
