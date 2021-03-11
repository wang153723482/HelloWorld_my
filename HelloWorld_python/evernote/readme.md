用于同步yinxiang和evernote

yinxiang买了会员，流量够用，但是由于某些众所周知的原因，需要同步到evernote

第一步，先遍历yinxiang所有的笔记本，如果有新建的笔记本，需要先在evernote新建笔记本

第二步，遍历所有笔记本中的笔记，根据最后修改日期，判断是否需要将内容同步到evernote


Token这里需要注意，yinxiang和evernote获取的token地址不一样，用户名也不一定一样，在代码中也要时时注意是用yinxiang还是product（对应evernote），另外，还有一个sandbox

yinxiang获取开发者token
https://dev.yinxiang.com/doc/articles/dev_tokens.php

evernote获取开发者token
https://dev.evernote.com/doc/articles/dev_tokens.php

sandbox获取开发者token，也分了evernote和yinxiang
https://sandbox.evernote.com/api/DeveloperToken.action
https://sandbox.yinxiang.com/api/DeveloperToken.action
