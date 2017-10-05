package persistence

import model.Person
import util.PersistenceUtil

object PersonRepository : IRepository<Person> {
    override fun find(id: Long): Person? {
        val entityManager = PersistenceUtil.getEntityManager()
        val item: Person

        try {
            item = entityManager.find(Person::class.java, id)
        } catch (e: Exception) {
            return null
        }

        entityManager.close()
        return item
    }

    override fun findAll(): List<Person> {
        val entityManager = PersistenceUtil.getEntityManager()
        val items: List<Person>

        try {
            items = entityManager.createQuery("SELECT p FROM Person p", Person::class.java).resultList
        } catch (e: Exception) {
            return emptyList()
        }

        entityManager.close()
        return items
    }

    override fun remove(id: Long): Boolean {
        val entityManager = PersistenceUtil.getEntityManager()

        try {
            entityManager.transaction.begin()
            entityManager.remove(entityManager.find(Person::class.java, id))
            entityManager.transaction.commit()
        } catch (e: Exception) {
            return false
        }

        entityManager.close()
        return true
    }
}
