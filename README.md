# ecma6-test
We have an existing ecma5 project that we want to start converting to ecma6. 
The first thing we need to figure out in order to do this is how to get the existing
ecma5 compiled into a single file using an ecma6 transpiler.

I've provided a fab file that should grab jquery require and traceur using the 'setup'
task. It should also attempt to compile using traceur with 'compile'. dev.html
should work once setup has run, as it is just looking at src, and running javascript
as normal. live.html runs off the built files (and is what I am trying to get working).

So, the goal of this test project is simply to get a functioning ecma5 javascript
project (that uses require) to be compiled into a single file via a ecma6 transpiler
(and that transpiler can be any of them, no particular attachement to traceur)
