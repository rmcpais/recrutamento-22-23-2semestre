import 'package:flutter/material.dart';

import 'inner_menu.dart';

class Menu extends StatelessWidget {
  const Menu({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Menu',
      home: InnerMenu(),
    );
  }
}
