# Lucrative API
Calculates the winnings to your investments with this API. Actually, a lot of people invest around the world. No
matter if it is about cryptocurrencies or stock exchanges. But, how to manage a way to simulate your potential
winning at the market by the time?

The only thing you need is to enter required data and our API returns to you the result like a function concept.

*That's the reason because I created this API.*

## SUMMARY
1. [Dependencies](#dependencies)
2. [Endpoints](#endpoints)
   * [Request's Body](#requests-body)
   * [Specifics Requests Bodies](#specifics-request-bodies)
3. [Response Body](#requests-body)
4. [Links FAQ](#links-faq)
5. [Index Contents](#index-contents)

## Dependencies
Here you can see a `.json` with our basic project's dependencies, note that at the end of the
page we've a **Links FAQ** to help you to install them.

```json
{
   "Python_3": "Our Chosen Programming Language.",
   "Virtualenv": "Project Local Python Interpreter.",
   "Pip": "Manage and install packages to your .venv",
   "FastAPI": "Our Used API Model.",
   "Uvicorn": "Our Server to Test Our API.",
   "Pydantic": "Our Library to Use as a Request Model."
}
```

> I strongly suggest you install these dependencies into a project local python installation.
> 
> At this project, we have the file `requirements.txt`, after activate your `.venv`, run:
> 
> $ `pip install -r requirements.txt`
>
> Our Links are in [Links FAQ](#links-faq)

## Endpoints

Here you find a `.json` with all links of this API.

```json
{
   "post-earning": "/api/lucrative/earning",
   "post-earnings": "/api/lucrative/earnings",
   "post-amounts": "/api/lucrative/amounts",
   "post-multi-earnings": "/api/lucrative/multi-earnings"
}
```

### Request's Body

In general we have **2** standards to our requests bodies. They are:

> `post-earning` and `post-earnings` and `post-amounts`
```json
{
   "money": 0,
   "descript": "string",
   "time": 1,
   "earn_rate": 0.2,
   "is_multi": false
}
```

>> **NOTE:** the parameter `descript` are **Optional**, in case of the endpoints:
>>
>> `post-earnings`
>>
>> `post-amounts`
>>
>> `post-multi-earnings`
>>
>> It is not need because the API override it.
> 
>> In `post_earning` it is just Optional.

> `post-multi-earnings`
```json
{
   "money": 0,
   "min_money": 0.5,
   "my_earnings": [
      {
         "money": 0,
         "descript": "string",
         "time": 1,
         "earn_rate": 0.2,
         "is_multi": false
      }
   ]
}
```

But there's some fields which are **optionals** *(they can be ignored)*, mainly at the first request
body here. So, I separated an option to solve them.

### Specifics Request Bodies
Now I present the specifics request bodies from context.
> `post-earning`
```json
{
   "money": 1000,
   "earn_rate": 0.2
}
```

> `post-earnings` Note: `time > 1 and is_multi == true` **required** always.
```json
{
   "money": 100,
   "time": 3000,
   "earn_rate": 0.05,
   "is_multi": true
}
```

> `post-amounts` Note: `time > 1 and is_multi == true` **required** always.
```json
{
   "money": 100,
   "time": 3000,
   "earn_rate": 0.05,
   "is_multi": true
}
```

> `post-multi-earnings` Note: `is_mult == true` **required** always.
```json
{
   "money": 10,
   "min_money": 0.5,
   "my_earnings": [
      {
         "earn_rate": 1.2,
         "is_multi": true
      }
   ]
}
```

## Response Body
Here I present to you our response model. It's basically a `.json`.

```json
{
   "capital": 0.00,
   "lucre_up": 0.00,
   "earn_rate": 0.00,
   "amount": 0.00,
   "time": 0.00,
   "descript": "string",
   "is_multi": false
}
```

## Links FAQ
1. [Python](https://www.python.org/)
2. [Pip](https://pypi.org/project/pip/)
3. [FastAPI](https://fastapi.tiangolo.com/)
4. [Uvicorn](https://www.uvicorn.org/)
5. [Pydantic](https://docs.pydantic.dev/)

<details>
    <summary>How to Install Python?</summary>
    <p>
        If you use a Linux based system, it's possible to you have python installed.
    </p>
    <details>
        <summary>Windows</summary>
        <p>
            Find Here: 
            <a href="https://www.python.org/downloads/windows/">
                Link
            </a>
        </p>
    </details>
    <details>
        <summary>MacOS</summary>
        <p>
            Find Here: 
            <a href="https://www.python.org/downloads/macos/">
                Link
            </a>
        </p>
    </details>
    <details>
        <summary>Other</summary>
        <p>
            Find Here: 
            <a href="https://www.python.org/downloads/other/">
                Link
            </a>
        </p>
    </details>
</details>
<br>
<details>
    <summary>How to create and activate a Virtualenv?</summary>
    <details>
            <summary>Pycharm</summary>
            <p>
                <a href="https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html">
                    Create Venv
                </a>
            </p>
            <p>
                Auto-activate.
            </p>
        </details>
    <details>
            <summary>Generate (Python docs)</summary>
            <p>
                <a href="https://docs.python.org/3/library/venv.html">
                    Generate Venv
                </a>
            </p>
        </details>
    <details>
        <summary>With Pip</summary>
        <p>
            <code>pip install virtualenv</code>
        </p>
    </details>
    <details>
        <summary>Activate</summary>
        <details>
            <summary>Linux and MacOS</summary>
            <p>
                <code>. venv/bin/activate</code> or
                <code>source venv/bin/activate</code>
            </p>
        </details>
        <details>
            <summary>Windows</summary>
            <p>
                <code>. venv/Scripts/Activate</code> or
                <code>source venv/Scripts/Activate</code>
            </p>
        </details>
    </details>
    <details>
        <summary>Deactivate</summary>
        <p>
            Just type <code>deactivate</code>
        </p>
    </details>
</details>
<br>
<details>
    <summary>How to install pip?</summary>
    <p>
        By default, <code>pip</code> is installed together python.
    </p>
</details>
<br>
<details>
    <summary>How to Install Fast API?</summary>
    <p>
        <code>pip install fastapi</code>
    </p>
</details>
<br>
<details>
    <summary>How to Install Uvicorn?</summary>
    <p>
        <code>pip install "uvicorn[standard]"</code>
    </p>
</details>
<br>
<details>
    <summary>How to Install Pydantic?</summary>
    <p>
        <code>pip install pydantic</code>
    </p>
</details>

## Index Contents
1. [Dependencies](#dependencies)
2. [Endpoints](#endpoints)
   * [Request's Body](#requests-body)
   * [Specifics Requests Bodies](#specifics-request-bodies)
3. [Response Body](#requests-body)
4. [Links FAQ](#links-faq)
5. [SUMMARY](#summary)

> **NOTE**: If you are interesting to learn how to do this documentation file, you can access:
> [MarkDown](https://www.markdownguide.org/).