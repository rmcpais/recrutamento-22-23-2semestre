import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:rss_bacano/rss.dart';
import 'package:shared_preferences/shared_preferences.dart';



class FeedApp extends StatelessWidget {
  const FeedApp({super.key});
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData(primarySwatch: Colors.green),
      title: 'Feed List',
      home: const FeedList(),
    );
  }
}


class FeedList extends StatefulWidget {
  const FeedList({super.key});
  @override
  FeedListState createState() => FeedListState();
}

class FeedListState extends State<FeedList> {
  final TextEditingController _titleFieldController = TextEditingController();
  final TextEditingController _urlFieldController = TextEditingController();
  List<Feed> _feeds = <Feed>[];
  late SharedPreferences saved;


  Future<void> _displayDialog() async {
    return showDialog<void>(
      context: context,
      barrierDismissible: false,
      builder: (BuildContext context) {
        return AlertDialog(
          title: const Text('Add a new RSS Feed'),
          content: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            mainAxisSize: MainAxisSize.min,
            children: [
              TextField(
                controller: _titleFieldController,
                decoration: const InputDecoration(hintText: 'Type a title'),
              ),
              TextField(
                controller: _urlFieldController,
                decoration: const InputDecoration(hintText: 'Type the Feed Url'),
              ),
            ],
          ),

          actions: <Widget>[
            TextButton(
              child: const Text('Add'),
              onPressed: () {
                Navigator.of(context).pop();
                _addFeedItem(_titleFieldController.text, _urlFieldController.text);
              },
            ),
          ],
        );
      },
    );
  }

  Future<void> _deleteFeedItem(Feed feed) async {
    setState(() {
      _feeds.remove(feed);
      saveFeeds();
    });
  }

  void saveFeeds(){
    List<String> savedList = _feeds.map((feed) => jsonEncode(feed.toMap())).toList();
    saved.setStringList('feeds', savedList);
  }

  void loadFeeds(){
    setState(() {
      List<String> savedList = saved.getStringList('feeds') as List<String>;
      _feeds = savedList.map((feed) => Feed.fromMap(json.decode(feed))).toList();
    });
  }

  void _addFeedItem(String name, String url) {
    setState(() {
      _feeds.add(Feed(name: name, strUrl: url));
      saveFeeds();
    });
    _titleFieldController.clear();
    _urlFieldController.clear();
  }

  void _handleFeedView(Feed feed){
    Navigator.push(
        context,
        MaterialPageRoute(builder: (context) => RSSFeed(feed.strUrl))
    );
  }


  @override
  void initState() {
    initSaved();
    super.initState();
  }

  initSaved() async {
    saved = await SharedPreferences.getInstance();
    loadFeeds();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Feed List'),
      ),
      body: ListView(
        padding: const EdgeInsets.symmetric(vertical: 8.0),
        children: _feeds.map((Feed feed){
          return FeedItem(
            feed: feed,
            onFeedClick: _handleFeedView,
            onDeleteButton: _deleteFeedItem,
          );
        }).toList(),
      ),
      floatingActionButton: FloatingActionButton(
          onPressed: () => _displayDialog(),
          tooltip: 'Add RSS Feed',
          child: const Icon(Icons.add)
      ),
    );

  }

}

class Feed {
  Feed({required this.name, required this.strUrl});
  final String name;
  final String strUrl;

  Feed.fromMap(Map map) :
        name = map['name'],
        strUrl = map['strUrl'];

  Map toMap(){
    return {
      'name': name,
      'strUrl': strUrl,
    };
  }
}

class FeedItem extends StatelessWidget{
  FeedItem({
    required this.feed,
    required this.onFeedClick,
    required this.onDeleteButton,
  }) : super(key: ObjectKey(feed));


  final Feed feed;
  final onFeedClick;
  final onDeleteButton;

  title(title) {
    return Text(
      title,
      style: const TextStyle(fontSize: 18.0, fontWeight: FontWeight.w500),
      maxLines: 2,
      overflow: TextOverflow.ellipsis,
    );
  }

  rightIcon() {
    return const Icon(
      Icons.keyboard_arrow_right,
      color: Colors.grey,
      size: 30,
    );
  }

  @override
  Widget build(BuildContext context) {
    return ListTile(
        leading: IconButton(
          icon: const Icon(Icons.delete),
          onPressed: () => onDeleteButton(feed),
        ),
        title: TextButton(
            onPressed: () => onFeedClick(feed),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: <Widget>[
                title(feed.name),
                rightIcon(),
              ],
            )
        )
    );
  }


}