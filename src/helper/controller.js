/**
 * Created by cj on 08/10/15.
 */

define(function (require) {
    var $ = require('jquery'),
        greeter = require('helper/greeter');
    $('body').html('Hello world...<br>');
    $('body').append(greeter.init());
});