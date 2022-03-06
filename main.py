import re

# zadanie 1
# # 1
input = 'Dzisiaj mamy 4 stopnie na plusie, 1 marca 2022 roku'
result = re.sub('\d',  '',    input)
print(result)

# # 2
input = '<div><h2>Header</h2> <p>article<b>strong text</b> <a href="">link</a> </p></div>'
result = re.sub('\<.{1,9}>',  ' ',    input)
print(result)

# #3
input = 'Lorem ipsum dolor sit amet, consectetur; adipiscing elit.' \
        'Sed eget mattis sem. Mauris egestas erat quam, ut faucibus eros congue et. In' \
        'blandit, mi eu porta; lobortis, tortor nisl facilisis leo, at tristique augue risus' \
        'eu risus.'
result = re.sub('[^\w\s]',  ' ',    input)
print(result)


# zadanie 2
input = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed #texting eget mattis sem. Mauris #frasista' \
        'egestas erat #tweetext quam, ut faucibus eros #frasier congue et. In blandit, mi eu porta' \
        'lobortis, tortor nisl facilisis leo, at tristique #frasistas augue risus eu risus.'
result = re.findall('#(\w+)',    input)
print(result)

# zadanie 3
input = 'Lorem ipsum dolor :) sit amet, consectetur; adipiscing elit. Sed eget mattis sem. ;) ' \
        'Mauris ;( egestas erat quam, :< ut faucibus eros congue :> et. In blandit, mi eu porta;' \
        'lobortis, tortor :-) nisl facilisis leo, at ;< tristique augue risus eu risus ;-).'
result = re.findall('[^\w\s]{2,3}',    input)
print(result)
