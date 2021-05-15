const router = require('express').Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/allproducts', function(req, res, next) {
  res.render('products', { title: 'Express' });
});

router.get('/product/:id', function(req, res, next) {
  res.render('product', { title: 'Express', productId: req.params.id });
});

router.get('/basket', function(req, res, next) {
  res.render('basket', { title: 'Express' });
});

router.get('/login', function(req, res, next) {
  res.render('login', { title: 'Express' });
});

router.get('/logout', function(req, res, next) {
  res.render('login', { title: 'Express' });
});

module.exports = router;
