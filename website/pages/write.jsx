import SimpleLayout from '../components/layout/simple'
import ArticlesJumbo from '../components/general/articles'

export default function Write(initialData) {
  return (
    <SimpleLayout preContainer={<ArticlesJumbo menu="About" />}>
      <div className="row">
        <h1>A few words about us</h1>
      </div>
      <div className="row">
        <p>
        {initialData.data.content.About}
        </p>
      </div>
    </SimpleLayout>
  )
}


// This gets called on every request
export async function getServerSideProps(context) {
  const host = context.req.headers.host
  // Fetch data from external API
  const res = await fetch(`http://${host}/data.json`)
  const data = await res.json()

  // Pass data to the page via props
  return { props: { data } }
}
