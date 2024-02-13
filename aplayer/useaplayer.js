const ap = new APlayer({
    container: document.getElementById('aplayer'),
    fixed: false,
    mini: false,
    listFolded: false,
    listMaxHeight: 90,
    lrcType: 3,
    audio: [
        {
            name: '西楼儿女',
            artist: '岳云鹏',
            url: 'https://dav.huwo.top/mp3/西楼儿女 - 岳云鹏.mp3',
            cover: 'https://dav.huwo.top/mp3/西楼儿女 - 岳云鹏.jpg',
            lrc: '/lrcs/西楼儿女 - 岳云鹏.lrc'
        },
        {
            name: '岁岁',
            artist: '任素汐',
            url: 'https://dav.huwo.top/mp3/岁岁 - 任素汐.mp3',
            cover: 'https://dav.huwo.top/mp3/岁岁 - 任素汐.png',
            lrc: '/lrcs/岁岁 - 任素汐.lrc'
        },
        {
            name: '胡广生',
            artist: '任素汐',
            url: 'https://dav.huwo.top/mp3/胡广生 - 任素汐.mp3',
            cover: 'https://dav.huwo.top/mp3/胡广生 - 任素汐.jpg',
            lrc: '/lrcs/胡广生 - 任素汐.lrc'
        },
        {
            name: '王招君',
            artist: '任素汐',
            url: 'https://dav.huwo.top/mp3/王招君 - 任素汐.mp3',
            cover: 'https://dav.huwo.top/mp3/王招君 - 任素汐.jpg',
            lrc: '/lrcs/王招君 - 任素汐.lrc'
        },
    ]
});