const Koa = require('koa');

const app = new Koa();

const one = (ctx, next)=>{
  console.log('one')
  next();
  console.log('ONE')
}

const two = (ctx, next)=>{
  console.log('two')
  next();
  console.log('TWO')
}

const three = (ctx, next)=>{
  console.log('three')
  next();
  console.log('THREE')
}

app.use(one)
app.use(two)
app.use(three)

app.listen(30003);

console.log('app started at port 30003...');