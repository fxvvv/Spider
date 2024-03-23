import pandas
import requests

L=[]
for page in range(1,20):

    headers = {
        'Accept': 'application/json',
        'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # Already added when you pass json=
        # 'Content-Type': 'application/json',
        # Requests sorts cookies= alphabetically
        # 'Cookie': 'll="118254"; bid=p0MbXH3C560; douban-fav-remind=1; viewed="1019568"; uaid="463930cab3ef9f57c6561d57780f661f443b7eff"; _ga=GA1.1.68034132.1711168608; _ga_RXNMP372GL=GS1.1.1711168608.1.1.1711169564.60.0.0',
        'Origin': 'https://read.douban.com',
        'Pragma': 'no-cache',
        'Referer': 'https://read.douban.com/category/103',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
        'X-CSRF-Token': '.eJwFwQkBACEIBMAuJpBdPCCOPPaPcDPLtKPAi7Mb8opftEyF9hjrEK5TWbLx_JCwsGuO7EZ4EusHTOIRbQ.Zf5gGw.CvDpwPt4iy898t03ZYlXNuWU5LA',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
    }

    json_data = {
        'sort': 'hot',
        'page': page,
        'kind': 103,
        'query': '\n    query getFilterWorksList($works_ids: [ID!]) {\n      worksList(worksIds: $works_ids) {\n        \n    id\n    isOrigin\n    isEssay\n    \n    title\n    cover(useSmall: false)\n    url\n    isBundle\n    coverLabel(preferVip: true)\n  \n    \n  url\n  title\n\n    \n  author {\n    name\n    url\n  }\n  origAuthor {\n    name\n    url\n  }\n  translator {\n    name\n    url\n  }\n\n    \n  abstract\n  authorHighlight\n  editorHighlight\n\n    \n    isOrigin\n    kinds {\n      \n    name @skip(if: true)\n    shortName @include(if: true)\n    id\n  \n    }\n    ... on WorksBase @include(if: true) {\n      wordCount\n      wordCountUnit\n    }\n    ... on WorksBase @include(if: false) {\n      inLibraryCount\n    }\n    ... on WorksBase @include(if: false) {\n      \n    isEssay\n    \n    ... on EssayWorks {\n      favorCount\n    }\n  \n    \n    \n    averageRating\n    ratingCount\n    url\n    isColumn\n    isFinished\n  \n  \n  \n    }\n    ... on EbookWorks @include(if: false) {\n      \n    ... on EbookWorks {\n      book {\n        url\n        averageRating\n        ratingCount\n      }\n    }\n  \n    }\n    ... on WorksBase @include(if: false) {\n      isColumn\n      isEssay\n      onSaleTime\n      ... on ColumnWorks {\n        updateTime\n      }\n    }\n    ... on WorksBase @include(if: true) {\n      isColumn\n      ... on ColumnWorks {\n        isFinished\n      }\n    }\n    ... on EssayWorks {\n      essayActivityData {\n        \n    title\n    uri\n    tag {\n      name\n      color\n      background\n      icon2x\n      icon3x\n      iconSize {\n        height\n      }\n      iconPosition {\n        x y\n      }\n    }\n  \n      }\n    }\n    highlightTags {\n      name\n    }\n    ... on WorksBase @include(if: false) {\n      fanfiction {\n        tags {\n          id\n          name\n          url\n        }\n      }\n    }\n  \n    \n  ... on WorksBase {\n    copyrightInfo {\n      newlyAdapted\n      newlyPublished\n      adaptedName\n      publishedName\n    }\n  }\n\n    isInLibrary\n    ... on WorksBase @include(if: false) {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on EbookWorks {\n      \n    fixedPrice\n    salesPrice\n    isRebate\n  \n    }\n    ... on WorksBase @include(if: true) {\n      ... on EbookWorks {\n        id\n        isPurchased\n        isInWishlist\n      }\n    }\n    ... on WorksBase @include(if: false) {\n      fanfiction {\n        fandoms {\n          title\n          url\n        }\n      }\n    }\n    ... on WorksBase @include(if: false) {\n      fanfiction {\n        kudoCount\n      }\n    }\n  \n      }\n    }\n  ',
        'variables': {},
    }

    response = requests.post('https://read.douban.com/j/kind/',  headers=headers, json=json_data)
    for i in response.json()['list']:
        title=i['title']
        try:
            origAuthor=i['origAuthor'][0]['name']
        except:
            origAuthor=i['author'][0]['name']
        abstract=i['abstract']
        url=i['id']
        print([title,origAuthor,abstract[0:10]+'...',url])
        L.append([title,origAuthor,abstract,url])


headers = {
    'Accept': 'application/json',
    'Accept-Language': 'zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    # Already added when you pass json=
    # 'Content-Type': 'application/json',
    # Requests sorts cookies= alphabetically
    # 'Cookie': 'll="118254"; bid=p0MbXH3C560; douban-fav-remind=1; viewed="1019568"; uaid="463930cab3ef9f57c6561d57780f661f443b7eff"; _ga=GA1.1.68034132.1711168608; _ga_RXNMP372GL=GS1.1.1711168608.1.1.1711169564.60.0.0',
    'Origin': 'https://read.douban.com',
    'Pragma': 'no-cache',
    'Referer': 'https://read.douban.com/category/103',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Edg/122.0.0.0',
    'X-CSRF-Token': '.eJwFwQkBACEIBMAuJpBdPCCOPPaPcDPLtKPAi7Mb8opftEyF9hjrEK5TWbLx_JCwsGuO7EZ4EusHTOIRbQ.Zf5gGw.CvDpwPt4iy898t03ZYlXNuWU5LA',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Chromium";v="122", "Not(A:Brand";v="24", "Microsoft Edge";v="122"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

for i in range(len(L)):
    book = L[i][3]

    json_data = {
        'operationName': 'getWorksComment',
        'query': '\n    query getWorksComment($worksId: ID!, $limit: Int) {\n      works: works(worksId: $worksId) {\n        worksType\n        ... on ColumnWorks {\n          columnId\n        }\n        \n    ... on WorksBase {\n      comments: mixedComments(limit: $limit) {\n        \n  ... on CommentBase {\n    id\n    isHidden\n    \n    \n  ... on CommentBase {\n    id\n    works {\n      agent {\n        id\n      }\n      \n  title\n  url\n  isChapter\n  isOnSale\n  hasOwned\n  agent {\n    id\n  }\n\n    }\n    user {\n      id\n      avatar: picture(size: MEDIUM)\n      avatarFrame\n      name\n      url\n      ... on Agent {\n        agentName\n        hasMedal\n        agentId\n      }\n    }\n    createTime\n    commentType\n    ... on Review {\n      url\n    }\n    \n  ... on Review {\n    badge {\n      url\n      image\n      title\n      color\n      label\n    }\n  }\n\n    ... on Annotation {\n      url\n      isPublic\n      isNote\n    }\n    \n  ... on WorksRecommend {\n    score\n    isEditorChoice\n  }\n\n  }\n  \n  ... on CommentBase {\n    works {\n      agent {\n        id\n      }\n    }\n    user {\n      id\n      isVip\n    }\n    hasPurchasedAllBadge\n  }\n  ... on Discussion {\n    donation {\n      amount\n    }\n  }\n\n\n    \n  ... on CommentBase {\n    id\n    content\n    commentType\n    works {\n      agent {\n        id\n      }\n    }\n    user {\n      id\n      ... on Agent {\n        agentName\n      }\n    }\n    ... on Discussion {\n      refComment {\n        id\n        user {\n          id\n          name\n          url\n          ... on Agent {\n            agentName\n            agentId\n          }\n        }\n        \n        createTime\n        content\n      }\n    }\n    ... on Review {\n      title\n    }\n    \n  ... on Review {\n    badge {\n      url\n      image\n      title\n      color\n      label\n    }\n  }\n\n    ... on Annotation {\n      \n  ... on Annotation {\n    originContent {\n      rawTexts {\n        text\n        type\n      }\n      startOffset\n      endOffset\n    }\n  }\n\n    }\n    ... on WorksRecommend {\n      title\n    }\n    ... on ReviewComment {\n      refComment {\n        id\n        content\n        createTime\n        \n        user {\n          id\n          name\n          ... on Agent {\n            agentName\n            agentId\n          }\n        }\n      }\n    }\n    ... on AnnotationComment {\n      refComment {\n        id\n        content\n        createTime\n        \n        user {\n          id\n          name\n          ... on Agent {\n            agentName\n            agentId\n          }\n        }\n      }\n    }\n    ... on WorksRecommendComment {\n      refComment {\n        id\n        content\n        createTime\n        \n        user {\n          id\n          name\n          ... on Agent {\n            agentName\n            agentId\n          }\n        }\n      }\n    }\n  }\n\n    \n  ... on CommentBase {\n    id\n    commentType\n    isHidden\n    \n    content\n    user {\n      id\n      name\n      isBlocked\n      ... on Agent {\n        agentName\n      }\n    }\n    works {\n      id\n      cover(useSmall: true)\n      title\n      \n  title\n  url\n  isChapter\n  isOnSale\n  hasOwned\n  agent {\n    id\n  }\n\n      agent {\n        id\n      }\n    }\n    \n    ... on Review {\n      url\n      upvoted\n      upvoteCount\n      commentCount\n      works {\n        isFanfiction\n        markAsFinished\n      }\n    }\n    ... on Annotation {\n      url\n      upvoted\n      upvoteCount\n      commentCount\n      isPublic\n      isNote\n      \n  ... on Annotation {\n    originContent {\n      rawTexts {\n        text\n        type\n      }\n      startOffset\n      endOffset\n    }\n  }\n\n    }\n    ... on Discussion {\n      targetId\n      upvoted\n      upvoteCount\n      works {\n        title\n        url\n      }\n    }\n    ... on WorksRecommend {\n      url\n      upvoted\n      upvoteCount\n      commentCount\n    }\n    ... on ReviewComment {\n      targetId\n      upvoted\n      upvoteCount\n    }\n    ... on AnnotationComment {\n      targetId\n      upvoted\n      upvoteCount\n    }\n    ... on WorksRecommendComment {\n      targetId\n      upvoted\n      upvoteCount\n    }\n  }\n\n    \n  ... on WorksRecommend {\n    id\n    works {\n      id\n      \n    title\n    cover(useSmall: true)\n    url\n    isBundle\n    coverLabel(preferVip: true)\n  \n      \n  url\n  title\n\n      \n  author {\n    name\n    url\n  }\n  origAuthor {\n    name\n    url\n  }\n  translator {\n    name\n    url\n  }\n\n      isColumn\n      isFinished\n      wordCount\n      wordCountUnit\n      isInLibrary\n    }\n  }\n\n    \n  ... on CommentBase {\n    id\n    commentType\n    content\n    works {\n      id\n      title\n    }\n    user {\n      id\n      name\n      isBlocked\n      ... on Agent {\n        agentName\n      }\n    }\n    isHidden\n    \n    \n    ... on Review {\n      title\n      rating\n      upvoted\n      upvoteCount\n      commentCount\n      works {\n        isFanfiction\n      }\n    }\n    ... on Annotation {\n      upvoted\n      upvoteCount\n      commentCount\n    }\n    ... on WorksRecommend {\n      upvoted\n      upvoteCount\n      commentCount\n    }\n    ... on Discussion {\n      targetId\n    }\n    ... on ReviewComment {\n      targetId\n    }\n    ... on AnnotationComment {\n      targetId\n    }\n    ... on WorksRecommendComment {\n      targetId\n    }\n  }\n  \n  ... on CommentBase {\n    id\n    commentType\n    content\n    works {\n      id\n    }\n    user {\n      id\n      name\n      ... on Agent {\n        agentName\n      }\n    }\n  }\n\n  \n  ... on CommentBase {\n    id\n    commentType\n  }\n\n\n  }\n\n      }\n      commentTotal: mixedCommentCount\n    }\n  \n\n  ... on WorksBase {\n    id\n    title\n    isFanfiction\n    markAsFinished\n    isColumn\n    isFinished\n    isOnSale\n    review {\n      id\n      content\n      ... on Review {\n        title\n        url\n        rating\n      }\n    }\n  }\n  ... on WorksBase @include(if: false) {\n    rating {\n      rating\n    }\n  }\n\n      }\n    }\n  ',
        'variables': {'worksId': book, 'limit': 10},
    }
    resposn_book = requests.post(url='https://read.douban.com/j/graphql?name=getWorksComment', headers=headers, json=json_data)
    for comment in resposn_book.json()['data']['works']['comments']:
        print(comment['content'])
        c = L[i]
        c.append(comment['content'])
    L[i] = c

df = pandas.DataFrame(L)
df.to_excel(index=False,excel_writer='豆瓣读书.xlsx')