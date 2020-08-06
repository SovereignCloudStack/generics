#!/bin/bash

mkdir -p test
stat test/wait >/dev/null 2>/dev/null || echo "#!/bin/bash" > test/wait && chmod +x test/wait
stat test/test >/dev/null 2>/dev/null || echo "#!/bin/bash" > test/test && chmod +x test/test
