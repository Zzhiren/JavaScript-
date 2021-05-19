const Koa = require('koa');
const router = require('koa-router')();// 注意require('koa-router')反悔的是函数
const bodyParser = require('koa-bodyparser');

// 创建一个Koa对象表示web app本身
const app = new Koa();

app.use(bodyParser());

// 对于任何请求，app将调用该异步函数处理请求
app.use(async (ctx, next) => {
  console.log(`${ctx.request.method} ${ctx.request.url}`); //打印url
  await next(); //调用下一个middleware
})

// add url-router
router.get('/hello/:name', async (ctx, next) =>{
  var name = ctx.params.name;
  ctx.response.body = `<h1>Hello, ${name}!</h1>`;
})

router.get('/', async (ctx, next) =>{
  ctx.response.body = `<h1>Index</h1>
    <form action="/signin" method="post">
      <p>Name: <input name="name" value="koa"></p>
      <p>Password: <input name="password" type="password"></p>
      <p><input type="submit" value="Submit"></p>
    </form>`;
})

router.post('/signin', async (ctx, next)=>{
  var name = ctx.request.body.name || '';
  var password = ctx.request.body.password || '';
  console.log(`signin width name: ${name}, password: ${password}`);
  if(name === 'koa' && password === '123456'){
    ctx.response.body = `<h1>Welcome, ${name}!</h1>`;
  }else{
    ctx.response.body = `<h1>Login failed!</h1>
    <p><a href="/">Try again</a></p>`;
  }
})

// add router middleware
app.use(router.routes())

app.listen(30003);

console.log('app started at port 30003...');