# ***Semi-Supervised Learning***
- ***কিছু লেবেলযুক্ত (labeled) ডেটা এবং বেশিরভাগ লেবেলবিহীন (unlabeled) ডেটা একসাথে ব্যবহার করা হয়।***
- ***যে ডেটার লেবেল আছে তা শেখে, কিন্তু লেবেলবিহীন ডেটা থেকেও কিছু শেখার চেষ্টা করে।***  

***অনেক সময় ডেটা সংগ্রহ করা সহজ, কিন্তু লেবেল করা কঠিন, সময়সাপেক্ষ এবং ব্যয়বহুল।***  
***উদাহরণ: মেডিকেল ইমেজ → ডেটা অনেক, কিন্তু ডাক্তারকে লেবেল করানো কঠিন।***   
***এখানে Semi-Supervised Learning কাজে আসে।***  

- ***SSL মূলত দুই ধরনের ডেটা ব্যবহার করে:***  
  ***Labeled Data (X_labeled, Y_labeled) → ডেটা যেখানে আউটপুট লেবেল জানা আছে***  
  ***Unlabeled Data (X_unlabeled) → ডেটা যেটার লেবেল নেই***  
 
## ***Workflow:***   
- ***প্রথমে লেবেলড ডেটা দিয়ে মডেল ট্রেনিং করা।***   
- ***তারপর মডেলকে লেবেলবিহীন ডেটার ওপর প্রেডিকশন করতে বলা।***  
- ***যদি প্রেডিকশন confident হয়, সেটাকে নতুন লেবেল হিসেবে ধরে ট্রেনিং সেটে যোগ করা।***  
- ***পুনরায় মডেল ট্রেনিং করা।***  
- ***এভাবে মডেল ধীরে ধীরে লেবেলবিহীন ডেটার তথ্যও কাজে লাগাতে শেখে।***

---
## ***Common Methods***   
- ***Self-Training (Pseudo-Labeling)***  
  ***মডেল নিজের লেবেলবিহীন ডেটার জন্য লেবেল প্রেডিক্ট করে।***  
  ***confident predictions কে লেবেলড ডেটার সঙ্গে মিশিয়ে পুনরায় ট্রেন করা হয়।***  
- ***Consistency Regularization***  
  ***মডেল শেখে যে ডেটা augment করলে আউটপুট খুব বদলাবে না।***  
  ***উদাহরণ: ছবি rotate বা noise দেওয়া হলেও ক্লাস একই থাকা উচিত।***  
- ***Graph-Based Methods***  
  ***ডেটাকে nodes এবং edges হিসেবে রিপ্রেজেন্ট করা হয়।***  
  ***একই cluster-এর nodes একে অপরের লেবেল থেকে শেখে।***  
- ***Generative Models***  
  ***যেমন Variational Autoencoders (VAE) বা GANs ব্যবহার করা যায়।***  
  ***unlabeled data থেকে latent representation শেখানো হয়।***

---
# ***Label Propagation***    
***Label Propagation হলো Semi-Supervised Learning algorithm, যা graph-based method।***   
- ***এখানে ডেটাকে nodes (points) হিসেবে ধরা হয়।***  
- ***যদি দুইটি node খুব similar হয়, তাহলে তাদের মধ্যে edge দিয়ে connection দেওয়া হয়।***  
- ***লেবেল ছড়িয়ে দেওয়া হয় (propagate) graph-এর মধ্যে।***   
- ***মূল ধারণা: similar points একই লেবেল শেয়ার করবে।***   
- ***Labeled node থেকে unlabeled node-এ information ছড়িয়ে দেয়ার মাধ্যমে unlabeled node-কে predict করে।***

---
## ***How it Works***
***`Step 1`: Prepare data***  
- ***ধরো 5 points আছে, 2 labeled, 3 unlabeled***  

|***Node***|***Label***|
|---|---|
|***1***|***Red***|
|***2***|***?***|
|***3***|***?***|
|***4***|***Blue***|
|***5***|***?***|

***`Step 2`: Build graph using KNN***         
- ***প্রতিটি point-এর কাছের K neighbors খুঁজে edge বানাও***  
- ***বেশি similar neighbors → বেশি influence***

***Node 1 → neighbors: 2,3***  
***Node 2 → neighbors: 1,3***  
***Node 3 → neighbors: 2,4***  
***Node 4 → neighbors: 3,5***  
***Node 5 → neighbors: 3,4***  

***`Step 3`: Initialize labels***
- ***Labeled nodes = original label***
- ***Unlabeled nodes = unknown***

***`Step 4`: Propagate labels***
- ***Unlabeled nodes neighbors-এর label অনুসারে update হয়***
- ***Iteratively, প্রতিটি unlabeled node “সরাসরি neighbors থেকে শেখে”***  

***Iteration 1***  
***Node 2 → Node 1 influence → starts becoming Red***  
***Node 3 → Node 4 influence → starts becoming Blue***   
***Node 5 → Node 4 influence → starts becoming Blue***  

***Iteration 2***  
***Node 2 → influenced by Node1 (Red) + Node3 (mostly Blue) → still more Red***  
***Node 3 → influenced by Node2 (mostly Red) + Node4 (Blue) → more Blue***  
***Node 5 → influenced by Node3 + Node4 → mostly Blue***  

***`Step 5`: Convergence***
- ***কিছু iteration পর labels আর change হয় না***   
- ***Unlabeled nodes শেষমেষ neighbors influence অনুযায়ী label পায়***

***Final Labels***   
|***Node***|***Label***|***Predicted Label***|
|---|---|---|
|***1***|***Red***|***Red***|
|***2***|***?***|***Red***|
|***3***|***?***|***Blue***|
|***4***|***Blue***|***Blue***|
|***5***|***?***|***Blue***|

---
### ***Author***  
***Md. Rafiqul Islam***  
***CSE, CoU***  
