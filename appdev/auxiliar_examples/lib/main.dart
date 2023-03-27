import 'package:flutter/material.dart';
import 'package:auxiliar_examples/gallery/gallery.dart';
import 'package:auxiliar_examples/workshop/workshop_two.dart';

import 'package:auxiliar_examples/default/default.dart';
import 'package:auxiliar_examples/infinite_list/infinite_list.dart';
import 'package:auxiliar_examples/menu/menu.dart';

void main() {
  const String exemploId = "workshop_2";
  switch (exemploId) {
    case "workshop_2":
      runApp(const WorkshopTwo());
      break;
    case "gallery":
      runApp(const Gallery());
      return;
    case "infinite":
      runApp(const InfiniteList());
      return;
    case "menu":
      runApp(const Menu());
      return;
    default:
      runApp(const Default());
      return;
  }
}
