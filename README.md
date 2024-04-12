# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution:
> path: tokenB->tokenA->tokenD->tokenC->tokenB, tokenB balance=20.129888944077443
> tokenB to tokenA , amountIn= 5 , amountOut= 5.655321988655322
> tokenA to tokenD , amountIn= 5.655321988655322 , amountOut= 2.4587813170979333
> tokenD to tokenC , amountIn= 2.4587813170979333 , amountOut= 5.0889272933015155
> tokenC to tokenB , amountIn= 5.0889272933015155 , amountOut= 20.129888944077443

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution
> Slippage:
> 
> Slippage refers to the difference between the price you expect to pay for a trade and the actual price executed on the blockchain. This occurs because AMM prices are based on the current liquidity pool reserves, and large trades can temporarily shift these reserves, leading to a slightly worse price for the trader.
> 
> Uniswap V2 Addressing Slippage:
> 
> Uniswap V2 partially addresses slippage through a concept called price impact. When you set a swap on Uniswap, you can specify a maximum acceptable price impact. This tells the AMM how much the price can deviate from the quoted price before the trade fails. A higher tolerance allows for larger trades but increases the risk of slippage.
> function: require(amounts[amounts.length - 1] >= amountOutMin, 'UniswapV2Router: INSUFFICIENT_OUTPUT_AMOUNT'); where amountOutMin takes the price impact into account.

## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution
> 1.Prevent Flash Loan Attacks: Flash loans allow attackers to borrow a large amount of tokens, manipulate the AMM price, and repay the loan instantly. The minimum liquidity helps mitigate this by making it more expensive to manipulate the price pool.
> 2.Incentivize Fair Pricing: By removing a small amount of liquidity, Uniswap discourages adding tokens at an unfair price (e.g., one token for a very large amount of another). This helps maintain a more balanced pool and fairer pricing for users.

## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution: The specific formula used when depositing tokens into an existing Uniswap V2 liquidity pool ensures that the ratio of deposited tokens matches the current pool's reserve ratio. This maintains the price peg established by the initial liquidity providers.

## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution: A sandwich attack involves exploiting price manipulation strategies to profit at the expense of other traders. In a sandwich attack, the attacker places large buy or sell orders around a target trade (initiated by another trader) to manipulate the price in their favor.
> 
> This attack can impact traders initiating swaps by causing slippage and unfavorable prices. Traders may end up receiving less of the desired token or paying more than expected due to the artificial price movement caused by the sandwich attack. To mitigate this risk, traders should be cautious, use limit orders when possible, and be aware of unusual price movements that could indicate potential attacks.
